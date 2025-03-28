import psutil
import socket
import ipaddress
import subprocess
import platform
import netifaces
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Dict, List, Optional
import sys,os

# Scapy 导入处理（macOS 需要安装）
try:
    from scapy.layers.l2 import ARP, Ether
    from scapy.sendrecv import srp1
except ImportError:
    print("注意：未找到 Scapy 库，ARP 扫描功能不可用")
    print("安装建议：pip install scapy")
    ARP = None


@dataclass
class NetworkConfig:
    interface: str
    ip: str
    subnet: str
    gateway: Optional[str]


class NetworkScanner:
    def __init__(
            self,
            max_workers: int = 100,
            ping_timeout: int = 0.1,
            use_arp: bool = True,
            debug: bool = False
    ):
        self.max_workers = max_workers
        self.ping_timeout = ping_timeout
        self.use_arp = use_arp if ARP else False  # 自动禁用不可用的 ARP
        self.debug = debug
        self.os_type = platform.system().lower()
        self._interface_blacklist = [
            'anpi', 'awdl', 'utun', 'lo0',
            'bridge', 'stf', 'gif', 'XHC',
            'thunderbolt', 'ipsec', 'llw'
        ]

    def get_network_configs(self) -> Dict[str, NetworkConfig]:
        """获取有效的网络配置"""
        configs = {}
        gateways = netifaces.gateways()
        default_gateway = gateways.get('default', {}).get(netifaces.AF_INET, [])

        for interface, addrs in psutil.net_if_addrs().items():
            if self._should_skip_interface(interface):
                continue

            ipv4_info = self._get_ipv4_info(addrs)
            if not ipv4_info:
                continue

            subnet = self._build_subnet(ipv4_info)
            if not subnet:
                continue

            configs[interface] = NetworkConfig(
                interface=interface,
                ip=ipv4_info.address,
                subnet=subnet,
                gateway=self._find_gateway(interface, default_gateway)
            )

        return configs

    def _should_skip_interface(self, interface: str) -> bool:
        """判断是否跳过接口"""
        if any(p in interface.lower() for p in self._interface_blacklist):
            return True
        stats = psutil.net_if_stats().get(interface)
        return not (stats and stats.isup)

    def _get_ipv4_info(self, addrs) -> Optional[psutil._common.snicaddr]:
        """获取 IPv4 地址信息"""
        for addr in addrs:
            if addr.family == socket.AF_INET:
                return addr
        return None

    def _build_subnet(self, ipv4_info) -> Optional[str]:
        """构建子网 CIDR 表示"""
        try:
            netmask = ipv4_info.netmask
            if not netmask:
                return None
            cidr = self.netmask_to_prefix(netmask)
            return f"{ipv4_info.address}/{cidr}"
        except (ValueError, AttributeError) as e:
            if self.debug:
                print(f"子网构建失败: {str(e)}")
            return None

    def _find_gateway(self, interface: str, gateways) -> Optional[str]:
        """查找接口对应的网关"""
        for gw_info in gateways:
            if gw_info[1] == interface:
                return gw_info[0]
        return None

    @staticmethod
    def netmask_to_prefix(netmask: str) -> int:
        """子网掩码转 CIDR 前缀"""
        return sum(bin(int(octet)).count('1') for octet in netmask.split('.'))

    def host_discovery(self, ip: str) -> bool:
        """主机存活检测"""
        if self.use_arp and self._is_local_network(ip):
            return self._arp_ping(ip)
        return self._icmp_ping(ip)

    def _is_local_network(self, ip: str) -> bool:
        """判断是否为本地网络（ARP 有效范围）"""
        try:
            return ipaddress.ip_address(ip).is_private
        except ValueError:
            return False

    def _icmp_ping(self, ip: str) -> bool:
        """ICMP ping 实现"""
        params = {
            'timeout': self.ping_timeout,
            'stdout': subprocess.DEVNULL,
            'stderr': subprocess.DEVNULL
        }

        if self.os_type == 'windows':
            cmd = ['ping', '-n', '1', '-w', str(self.ping_timeout * 1000), ip]
        else:
            cmd = ['ping', '-c', '1', '-W', str(self.ping_timeout), ip]

        try:
            return subprocess.run(cmd, **params).returncode == 0
        except Exception as e:
            if self.debug:
                print(f"Ping {ip} 失败: {str(e)}")
            return False

    def _arp_ping(self, ip: str) -> bool:
        """ARP 扫描实现"""
        try:
            pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
            resp = srp1(pkt, timeout=1, verbose=0)
            return resp is not None
        except Exception as e:
            if self.debug:
                print(f"ARP {ip} 失败: {str(e)}")
            return False

    def scan_network(self, config: NetworkConfig):
        """扫描指定网络接口"""
        try:
            network = ipaddress.ip_network(config.subnet, strict=False)
            if network.prefixlen > 30:
                if self.debug:
                    print(f"跳过无效子网 {config.subnet}")
                return
        except ValueError as e:
            print(f"无效的子网 {config.subnet}: {str(e)}")
            return

        print(f"开始扫描 {config.interface} ({config.subnet})...")
        alive_hosts = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._check_host, str(ip), config): ip
                for ip in network.hosts()
            }
            for future in as_completed(futures):
                if result := future.result():
                    alive_hosts.append(result)

        self._save_results(config.interface, alive_hosts)

    def _check_host(self, ip: str, config: NetworkConfig) -> Optional[str]:
        """检查单个主机"""
        if ip == config.ip or ip == config.gateway:
            return None
        return ip if self.host_discovery(ip) else None

    def _save_results(self, interface: str, hosts: List[str]):
        """保存扫描结果"""
        if not hosts:
            print(f"{interface} 未发现存活主机")
            return

        filename = f"{interface}_scan.log"
        try:
            with open(filename, 'w') as f:
                f.write("\n".join(hosts) + "\n")
            print(f"发现 {len(hosts)} 台主机，结果已保存到 {filename}")
        except IOError as e:
            print(f"保存 {filename} 失败: {str(e)}")

def main():
    # 参数配置
    scanner = NetworkScanner(
        max_workers=100,  # 并发线程数
        use_arp=True,  # 优先使用 ARP 扫描
        debug=False  # 调试模式
    )

    configs = scanner.get_network_configs()
    if not configs:
        print("未找到有效网络接口")
        return

    print("发现以下网络接口:")
    for cfg in configs.values():
        print(f" - {cfg.interface:8} {cfg.subnet} (网关: {cfg.gateway or '无'})")

    with ThreadPoolExecutor() as executor:
        executor.map(scanner.scan_network, configs.values())


if __name__ == "__main__":
    # macOS 需要 root 权限执行 ARP 扫描
    if platform.system() == 'Darwin' and ARP and os.geteuid() != 0:
        print("注意：ARP 扫描需要 root 权限，请使用 sudo 执行！")
        sys.exit(1)

    main()