#!/usr/bin/env python3
import os
import sys
import socket
import threading
import concurrent.futures
from tkinter import *
from tkinter import ttk, filedialog
import psutil
import ipaddress
from scapy.layers.l2 import ARP, Ether
from scapy.layers.inet import ICMP, IP
from scapy.sendrecv import srp, sr1


class NetworkScannerPro(Tk):
    def __init__(self):
        super().__init__()
        self.title("局域网嗅探工具 v1.1")
        self.geometry("1024x768")
        self._setup_ui()
        self.running = False
        self.threads = []
        self.thread_lock = threading.Lock()
        self.active_ips = {}
        self._initialize_data()

    def _setup_ui(self):
        """初始化用户界面"""
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)

        # 工具栏
        toolbar = ttk.Frame(main_frame)
        self._create_toolbar_buttons(toolbar)
        toolbar.pack(fill=X, pady=5)

        # 接口列表
        tree_frame = ttk.Frame(main_frame)
        self._setup_interface_tree(tree_frame)
        tree_frame.pack(fill=BOTH, expand=True, pady=5)

        # 配置区域
        config_frame = ttk.LabelFrame(main_frame, text="扫描配置")
        self._setup_config_controls(config_frame)
        config_frame.pack(fill=X, pady=10)

        # 控制按钮
        self._setup_control_buttons(main_frame)

        # 日志区域
        self._setup_log_area(main_frame)

    def _create_toolbar_buttons(self, parent):
        """创建工具栏按钮"""
        buttons = [
            ("刷新接口", self._refresh_interfaces),
            ("全选", self._select_all),
            ("取消全选", self._deselect_all),
            ("开始扫描", self._start_scan),
            ("停止扫描", self._stop_scan)
        ]
        for text, command in buttons:
            btn = ttk.Button(parent, text=text, command=command, width=12)
            btn.pack(side=LEFT, padx=3)

    def _setup_interface_tree(self, parent):
        """初始化接口列表"""
        self.tree = ttk.Treeview(parent, columns=("sel", "iface", "ip", "mask"),
                                 show="headings", height=10)

        # 列配置
        columns = [
            ("sel", "✓", 40, CENTER),
            ("iface", "网络接口", 220, W),
            ("ip", "IP地址", 180, W),
            ("mask", "子网掩码", 150, W)
        ]
        for col, text, width, anchor in columns:
            self.tree.heading(col, text=text)
            self.tree.column(col, width=width, anchor=anchor)

        # 滚动条
        vsb = ttk.Scrollbar(parent, orient=VERTICAL, command=self.tree.yview)
        hsb = ttk.Scrollbar(parent, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # 布局
        self.tree.grid(row=0, column=0, sticky=NSEW)
        vsb.grid(row=0, column=1, sticky=NS)
        hsb.grid(row=1, column=0, sticky=EW)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        # 事件绑定
        self.tree.bind("<Button-1>", self._handle_tree_click)

    def _setup_config_controls(self, parent):
        """初始化配置控件"""
        # 第一行
        row1 = ttk.Frame(parent)
        ttk.Label(row1, text="最大线程:").pack(side=LEFT)
        self.max_workers = ttk.Spinbox(row1, from_=1, to=500, width=8)
        self.max_workers.pack(side=LEFT, padx=5)
        self.max_workers.set(100)

        ttk.Label(row1, text="超时(秒):").pack(side=LEFT, padx=10)
        self.timeout = ttk.Spinbox(row1, from_=0.5, to=5.0, increment=0.1, width=8)
        self.timeout.set(1.0)
        self.timeout.pack(side=LEFT)
        row1.pack(anchor=W, pady=3)

        # 第二行
        row2 = ttk.Frame(parent)
        ttk.Label(row2, text="扫描模式:").pack(side=LEFT)
        self.scan_mode = ttk.Combobox(row2, values=["智能模式", "ARP扫描", "ICMP扫描"],
                                      width=12, state="readonly")
        self.scan_mode.current(0)
        self.scan_mode.pack(side=LEFT, padx=5)

        ttk.Label(row2, text="子网掩码:").pack(side=LEFT, padx=10)
        self.subnet_mask = ttk.Combobox(row2, values=["/24", "/16", "255.255.255.0"],
                                        width=12)
        self.subnet_mask.current(0)
        self.subnet_mask.pack(side=LEFT)
        row2.pack(anchor=W, pady=3)

        # 第三行
        row3 = ttk.Frame(parent)
        ttk.Label(row3, text="保存路径:").pack(side=LEFT)
        self.save_path = ttk.Entry(row3, width=35)
        self.save_path.pack(side=LEFT, padx=5)
        self.save_path.insert(0, os.path.expanduser("~/scan_results"))
        ttk.Button(row3, text="浏览...", command=self._select_save_path).pack(side=LEFT)
        row3.pack(anchor=W, pady=3)

    def _setup_control_buttons(self, parent):
        """初始化控制按钮"""
        btn_frame = ttk.Frame(parent)
        self.start_btn = ttk.Button(btn_frame, text="开始扫描", command=self._start_scan, width=15)
        self.start_btn.pack(side=LEFT, padx=10)
        self.stop_btn = ttk.Button(btn_frame, text="停止扫描", state=DISABLED,
                                   command=self._stop_scan, width=15)
        self.stop_btn.pack(side=LEFT)
        btn_frame.pack(pady=10)

    def _setup_log_area(self, parent):
        """初始化日志区域"""
        self.log = Text(parent, height=12, state=DISABLED)
        vsb = ttk.Scrollbar(parent, orient=VERTICAL, command=self.log.yview)
        self.log.configure(yscrollcommand=vsb.set)
        self.log.pack(side=LEFT, fill=BOTH, expand=True)
        vsb.pack(side=RIGHT, fill=Y)

    def _initialize_data(self):
        """初始化数据"""
        self._refresh_interfaces()

    def _refresh_interfaces(self):
        """刷新接口列表"""
        selected = [self.tree.item(i)["values"][1] for i in self.tree.get_children()]

        self.tree.delete(*self.tree.get_children())
        for name, addrs in psutil.net_if_addrs().items():
            ipv4 = next((a for a in addrs if a.family == socket.AF_INET), None)
            ip = ipv4.address if ipv4 else "无IP地址"
            mask = ipv4.netmask if ipv4 else "N/A"
            state = "☑" if name in selected else "□"
            self.tree.insert("", "end", values=(state, name, ip, mask))

    def _handle_tree_click(self, event):
        """处理树状列表点击"""
        region = self.tree.identify("region", event.x, event.y)
        if region == "cell":
            col = self.tree.identify_column(event.x)
            item = self.tree.identify_row(event.y)
            if col == "#1":
                current = self.tree.set(item, "sel")
                self.tree.set(item, "sel", "☑" if current == "□" else "□")

    def _select_all(self):
        """全选接口"""
        for item in self.tree.get_children():
            self.tree.set(item, "sel", "☑")

    def _deselect_all(self):
        """取消全选"""
        for item in self.tree.get_children():
            self.tree.set(item, "sel", "□")

    def _select_save_path(self):
        """选择保存路径"""
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            initialfile=self.save_path.get()
        )
        if path:
            self.save_path.delete(0, END)
            self.save_path.insert(0, path)

    def _start_scan(self):
        """启动扫描"""
        if self.running:
            return

        try:
            max_workers = int(self.max_workers.get())
            timeout = float(self.timeout.get())
        except ValueError:
            self._log("错误：无效的数值参数")
            return

        selected = [self.tree.item(i)["values"]
                    for i in self.tree.get_children()
                    if self.tree.set(i, "sel") == "☑"]
        if not selected:
            self._log("错误：请选择至少一个接口")
            return

        self.running = True
        self.start_btn.config(state=DISABLED)
        self.stop_btn.config(state=NORMAL)
        self.active_ips.clear()
        self._log("=== 扫描开始 ===")

        with self.thread_lock:
            self.threads = []
            for iface_info in selected:
                thread = threading.Thread(target=self._scan_interface, args=(iface_info,))
                thread.start()
                self.threads.append(thread)

    def _scan_interface(self, iface_info):
        """执行接口扫描"""
        _, name, ip, _ = iface_info
        if ip == "无IP地址":
            self._log(f"[{name}] 接口无有效IP，跳过")
            return

        try:
            mask = self.subnet_mask.get()
            prefix = self._netmask_to_prefix(mask)
            network = ipaddress.IPv4Network(f"{ip}/{prefix}", strict=False)
            targets = [str(host) for host in network.hosts()]

            with concurrent.futures.ThreadPoolExecutor(
                    max_workers=int(self.max_workers.get())) as executor:

                futures = [executor.submit(self._check_host, name, ip_addr,
                                           self.scan_mode.get(),
                                           float(self.timeout.get()))
                           for ip_addr in targets]

                self.active_ips[name] = []
                for future in concurrent.futures.as_completed(futures):
                    if not self.running:
                        break
                    result = future.result()
                    if result:
                        self.active_ips[name].append(result)
                        self._log(f"[{name}] 发现主机：{result}")

            self._save_results(name)
            self._log(f"[{name}] 扫描完成，保存至：{self.save_path.get()}_{name}.txt")

        except Exception as e:
            self._log(f"[{name}] 扫描错误：{str(e)}")
        finally:
            with self.thread_lock:
                if threading.current_thread() in self.threads:
                    self.threads.remove(threading.current_thread())
                if not self.threads:
                    self.after(0, self._scan_complete)

    def _scan_complete(self):
        """扫描完成处理"""
        self.running = False
        self.start_btn.config(state=NORMAL)
        self.stop_btn.config(state=DISABLED)
        self._log("=== 所有扫描任务完成 ===")

    def _check_host(self, interface, ip_addr, mode, timeout):
        """主机存活检测"""
        try:
            if mode == "智能模式":
                if ipaddress.IPv4Address(ip_addr).is_private:
                    return self._arp_scan(interface, ip_addr, timeout)
                return self._icmp_ping(ip_addr, timeout)
            elif mode == "ARP扫描":
                return self._arp_scan(interface, ip_addr, timeout)
            else:
                return self._icmp_ping(ip_addr, timeout)
        except:
            return None

    @staticmethod
    def _netmask_to_prefix(netmask):
        """子网掩码转换"""
        if netmask.startswith('/'):
            return int(netmask[1:])
        elif netmask.startswith('0x'):
            return bin(int(netmask[2:], 16)).count('1')
        else:
            return sum(bin(int(octet)).count('1') for octet in netmask.split('.'))

    @staticmethod
    def _arp_scan(interface, ip_addr, timeout):
        """执行ARP扫描"""
        packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_addr)
        ans, _ = srp(packet, timeout=timeout, verbose=0, iface=interface)
        return ip_addr if ans else None

    @staticmethod
    def _icmp_ping(ip_addr, timeout):
        """执行ICMP Ping"""
        packet = IP(dst=ip_addr) / ICMP()
        resp = sr1(packet, timeout=timeout, verbose=0)
        return ip_addr if resp else None

    def _save_results(self, interface):
        """保存扫描结果"""
        base = self.save_path.get()
        active = self.active_ips.get(interface, [])

        if active:
            with open(f"{base}_{interface}.txt", "w") as f:
                f.write("\n".join(active))

        no_results = [k for k, v in self.active_ips.items() if not v]
        if no_results:
            with open(f"{base}_no_results.txt", "w") as f:
                f.write("\n".join(no_results))

    def _stop_scan(self):
        """停止扫描"""
        self.running = False
        with self.thread_lock:
            for t in self.threads:
                if t.is_alive():
                    t.join(timeout=0.5)
            self.threads.clear()
        self._scan_complete()
        self._log("=== 扫描已手动停止 ===")

    def _log(self, message):
        """线程安全日志记录"""
        self.log.config(state=NORMAL)
        self.log.insert(END, f"{message}\n")
        self.log.see(END)
        self.log.config(state=DISABLED)


if __name__ == "__main__":
    if sys.platform == 'darwin' and os.geteuid() != 0:
        print("注意：macOS需要root权限执行扫描！")
    app = NetworkScannerPro()
    app.mainloop()