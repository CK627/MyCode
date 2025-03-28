import PySimpleGUI as sg
import ipaddress
import platform
import os
import time
import threading
import psutil
import concurrent.futures
from scapy.all import *

conf.verb = 0

class DHCPUtils:
    @staticmethod
    def get_interfaces():
        try:
            return [iface.name for iface in get_working_ifaces()]
        except:
            return []

    @staticmethod
    def validate_mac(mac):
        return re.match(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", mac)

    @staticmethod
    def validate_cidr(cidr):
        try:
            network = ipaddress.IPv4Network(cidr, strict=False)
            return network.prefixlen < 32
        except:
            return False

    @staticmethod
    def check_permissions():
        import platform
        system = platform.system()
        if system == "Windows":
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        elif system in ["Darwin", "Linux"]:
            return os.getuid() == 0
        else:
            return False


class DHCPSenderGUI:
    def __init__(self):
        self.running = False
        self.log_queue = queue.Queue()
        self.log_lock = threading.Lock()
        self._check_permissions()
        self.window = self._create_gui()
        self._refresh_interfaces()

    def _check_permissions(self):
        if not DHCPUtils.check_permissions():
            sg.popup_error("需要管理员权限运行！\n"
                           "Windows: 右键使用管理员身份运行\n"
                           "macOS/Linux: 使用sudo执行",
                           title="权限错误")
            sys.exit(1)

    def _create_gui(self):
        sg.theme('DarkGrey5')

        layout = [
            [sg.Text("网络接口:", size=(10, 1)),sg.Combo([], key='-INTERFACE-', size=(30, 1), enable_events=True),sg.Button('刷新接口', key='-REFRESH-')],
            [sg.Frame('广播设置', [[sg.Radio('全网广播', "RADIO1", default=True, key='-GLOBAL-'),sg.Radio('指定网段', "RADIO1", key='-CIDR-'),sg.InputText('192.168.1.0/24', size=(15, 1), key='-CIDR_INPUT-')]])],
            [sg.Frame('客户端参数', [[sg.Text("MAC地址:", size=(10, 1)),sg.InputText(self._random_mac(), key='-MAC-', size=(20, 1)),sg.Button('随机生成', key='-RAND_MAC-')]]),
            [sg.HSeparator()],
            [sg.Column([
                [sg.Button('发送请求', key='-SEND-'), 
                 sg.Text("请求次数:"),
                 sg.Spin([i for i in range(1, 1000)], initial_value=1, key='-COUNT-', size=(5,1)),
                 sg.Button('开始压力测试', key='-STRESS-'),
                 sg.Text("线程数:"), 
                 sg.Spin([i for i in range(1, 50)], initial_value=10, key='-THREADS-', size=(5,1)),
                 sg.Button('停止', key='-STOP-', disabled=True),
                 sg.Exit()]
            ], pad=(0,10))],
            [sg.Multiline(size=(70, 10), key='-LOG-', autoscroll=True)]]
        ]

        return sg.Window("DHCP测试工具 Pro", layout, finalize=True)

    def _random_mac(self):
        return ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))

    def _refresh_interfaces(self):
        interfaces = DHCPUtils.get_interfaces()
        self.window['-INTERFACE-'].update(values=interfaces)
        if interfaces:
            self.window['-INTERFACE-'].update(value=interfaces[0])

    def _log(self, message, color='black'):
        with self.log_lock:
            self.log_queue.put((message, color))

    def run(self):
        while True:
            # 处理日志队列
            while not self.log_queue.empty():
                msg, color = self.log_queue.get()
                self.window['-LOG-'].print(msg, text_color=color)
            
            event, values = self.window.read(timeout=100)

            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            if event == '-REFRESH-':
                self._refresh_interfaces()
                self._log("接口列表已刷新", 'green')

            if event == '-RAND_MAC-':
                self.window['-MAC-'].update(self._random_mac())
                self._log("已生成随机MAC地址", 'blue')

            if event == '-SEND-':
                if self._validate_input(values):
                    Thread(target=self.send_packets, args=(values,), daemon=True).start()

            if event == '-STRESS-':
                self.running = True
                self.window['-STRESS-'].update(disabled=True)
                self.window['-STOP-'].update(disabled=False)
                Thread(target=self.stress_test, args=(values,), daemon=True).start()
                self._log("压力测试已启动", 'green')

            if event == '-STOP-':
                self.running = False
                self.window['-STRESS-'].update(disabled=False)
                self.window['-STOP-'].update(disabled=True)
                self._log("压力测试已停止", 'red')

        self.window.close()

    def _validate_input(self, values):
        if not DHCPUtils.validate_mac(values['-MAC-']):
            self._log("错误：MAC地址格式无效", 'red')
            return False

        if values['-CIDR-'] and not DHCPUtils.validate_cidr(values['-CIDR_INPUT-']):
            self._log("错误：CIDR格式无效", 'red')
            return False

        if not values['-INTERFACE-']:
            self._log("错误：请选择网络接口", 'red')
            return False

        return True

    def send_packets(self, values):
        try:
            count = int(values['-COUNT-'])
            for _ in range(count):
                self._send_packet(values)
                self._log(f"成功发送第{_ + 1}个请求", 'green')
        except Exception as e:
            self._log(f"发送错误：{str(e)}", 'red')

    def _send_packet(self, values):
        try:
            iface = values['-INTERFACE-']
            client_mac = values['-MAC-']
            dst_ip = '255.255.255.255' if values['-GLOBAL-'] else str(
                ipaddress.IPv4Network(values['-CIDR_INPUT-'], strict=False).broadcast_address
            )

            # 构建DHCP数据包（修正版）
            dhcp_packet = (
                    scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff") /
                    scapy.all.IP(src="0.0.0.0", dst=dst_ip) /
                    scapy.all.UDP(sport=68, dport=67) /
                    scapy.all.BOOTP(op=1, chaddr=mac2str(client_mac)) /  # 使用正确的mac2str函数
                    scapy.all.DHCP(options=[("message-type", "discover"), "end"])
            )

            sendp(dhcp_packet, iface=iface, verbose=0)

        except Exception as e:
            raise RuntimeError(f"发送失败：{str(e)}")

    def stress_test(self, values):
        self.window.write_event_value(('-STATUS_UPDATE-', ("压力测试启动中...", 'blue')), None)
        
        # 提取线程安全参数
        thread_count = int(values['-THREADS-'])
        task_count = int(values['-COUNT-'])
        iface = values['-INTERFACE-']
        client_mac = values['-MAC-']
        cidr = values['-CIDR_INPUT-'] if values['-CIDR-'] else '255.255.255.255'

        # 添加内存监控
        self._log(f"当前内存使用: {psutil.virtual_memory().percent}%", 'purple')
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
            futures = [executor.submit(self.worker, iface, client_mac, cidr) 
                      for _ in range(task_count)]
            
            try:
                for future in concurrent.futures.as_completed(futures):
                    if not self.running:
                        executor.shutdown(wait=False)
                        break
                    # 定期记录资源使用情况
                    if random.random() < 0.1:
                        self._log(f"内存使用: {psutil.virtual_memory().percent}% | 线程数: {thread_count}", 'purple')
            except Exception as e:
                self.window.write_event_value(('-STATUS_UPDATE-', (f"压力测试异常: {str(e)}", 'red')), None)
            finally:
                self.window.write_event_value(('-STOP_TEST-', None), None)
                self._log(f"最终内存占用: {psutil.virtual_memory().percent}%", 'purple')

    def worker(self, iface, client_mac, cidr):
        try:
            if self.running:
                # 使用线程安全参数构造数据包
                self._send_packet({
                    '-INTERFACE-': iface,
                    '-MAC-': client_mac,
                    '-CIDR_INPUT-': cidr,
                    '-GLOBAL-': cidr == '255.255.255.255'
                })
                self.window.write_event_value(('-STATUS_UPDATE-', ("请求发送成功", 'green')), None)
        except Exception as e:
            self.window.write_event_value(('-STATUS_UPDATE-', (f"请求失败: {str(e)}", 'red')), None)


if __name__ == "__main__":
    # 依赖检查
    try:
        import scapy
    except ImportError:
        sg.popup_error("需要安装Scapy库：pip install scapy")
        sys.exit(1)

    DHCPSenderGUI().run()