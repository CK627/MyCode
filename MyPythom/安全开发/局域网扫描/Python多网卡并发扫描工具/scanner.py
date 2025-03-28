import os
import sys
import platform
import ipaddress
import psutil
import netifaces
import socket
import subprocess
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import configparser

# 错误处理模块
try:
    from error_handler import ErrorHandler
except ImportError as e:
    print(f"致命错误：{str(e)}")
    sys.exit(1)

# Scapy导入处理
try:
    from scapy.layers.l2 import ARP, Ether
    from scapy.sendrecv import srp1
except ImportError as e:
    ErrorHandler.handle_import_error(e, "scapy")


@dataclass
class NetworkConfig:
    interface: str
    ip: str
    subnet: str


class ConfigLoader:
    REQUIRED_CONFIG = {
        'Network': [
            ('max_workers', int),
            ('ping_timeout', int),
            ('use_arp', 'bool'),
            ('debug_mode', 'bool'),
            ('scan_method', str)
        ]
    }

    def __init__(self, config_path: str = 'config.ini'):
        self.config = configparser.ConfigParser()
        self.config_path = Path(config_path)
        self._validate_config()
        self._load_config()

    def _validate_config(self):
        """严格配置验证"""
        if not self.config_path.exists():
            ErrorHandler.handle_config_error(f"配置文件 {self.config_path} 不存在")

        self.config.read(self.config_path)

        # 验证必须的配置段和配置项
        for section, items in self.REQUIRED_CONFIG.items():
            if not self.config.has_section(section):
                ErrorHandler.handle_config_error(f"缺失配置段 [{section}]")

            for key, dtype in items:
                if not self.config.has_option(section, key):
                    ErrorHandler.handle_config_error(f"缺失配置项 [{section}] {key}")

                value = self.config.get(section, key)
                if dtype == 'bool':
                    if value.lower() not in ['true', 'false', '1', '0']:
                        ErrorHandler.handle_config_error(f"非法布尔值 [{section}] {key}={value}")
                elif dtype == int:
                    if not value.isdigit():
                        ErrorHandler.handle_config_error(f"需要整数 [{section}] {key}={value}")

    def _load_config(self):
        """加载配置项"""
        self.config.read(self.config_path)

    def get_network_config(self) -> dict:
        """获取网络配置"""
        return {
            'max_workers': self.config.getint('Network', 'max_workers'),
            'ping_timeout': self.config.getint('Network', 'ping_timeout'),
            'use_arp': self._parse_bool('Network', 'use_arp'),
            'debug_mode': self._parse_bool('Network', 'debug_mode'),
            'scan_method': self.config.get('Network', 'scan_method'),
            'override_subnet': self.config.get('Network', 'override_subnet', fallback='')
        }

    def _parse_bool(self, section: str, key: str) -> bool:
        """解析布尔值配置"""
        val = self.config.get(section, key).lower()
        return val in ['true', '1']

    def get_output_config(self) -> dict:
        """获取输出配置"""
        return {
            'log_dir': Path(self.config.get('Output', 'log_dir')),
            'file_prefix': self.config.get('Output', 'file_prefix')
        }


class NetworkScanner:
    def __init__(self):
        self.config_loader = ConfigLoader()
        self.network_cfg = self.config_loader.get_network_config()
        self._prepare_environment()

    def _prepare_environment(self):
        """准备运行环境"""
        if platform.system() == 'Darwin' and self.network_cfg['use_arp'] and os.geteuid() != 0:
            print("\n[错误] ARP扫描需要root权限!")
            print("请使用以下命令重新运行:")
            print("sudo python3", *sys.argv)
            sys.exit(1)

    def get_network_configs(self) -> Dict[str, NetworkConfig]:
        """获取所有有效网络接口"""
        configs = {}
        for interface, addrs in psutil.net_if_addrs().items():
            ipv4_info = self._get_ipv4_info(addrs)
            if not ipv4_info:
                continue

            subnet = self._build_subnet(ipv4_info)
            if subnet:
                configs[interface] = NetworkConfig(
                    interface=interface,
                    ip=ipv4_info.address,
                    subnet=subnet
                )
                if self.network_cfg['debug_mode']:
                    print(f"[接口发现] {interface}: {ipv4_info.address} -> {subnet}")
        return configs

    def _get_ipv4_info(self, addrs) -> Optional[psutil._common.snicaddr]:
        """获取有效的IPv4地址信息"""
        for addr in addrs:
            if addr.family == socket.AF_INET and addr.address != '127.0.0.1':
                return addr
        return None

    def _build_subnet(self, ipv4_info) -> Optional[str]:
        """构建子网CIDR表示"""
        override = self.network_cfg['override_subnet']
        if override:
            try:
                # 处理不同格式的子网掩码
                if override.startswith('/'):
                    return f"{ipv4_info.address}{override}"
                elif override.startswith('0x'):
                    cidr = bin(int(override[2:], 16)).count('1')
                    return f"{ipv4_info.address}/{cidr}"
                else:
                    cidr = sum(bin(int(octet)).count('1') for octet in override.split('.'))
                    return f"{ipv4_info.address}/{cidr}"
            except Exception as e:
                print(f"无效的子网覆盖配置: {str(e)}")
                return None

        # 自动检测子网
        try:
            cidr = sum(bin(int(octet)).count('1') for octet in ipv4_info.netmask.split('.'))
            return f"{ipv4_info.address}/{cidr}"
        except Exception:
            return None

    def scan_network(self, config: NetworkConfig):
        """执行网络扫描"""
        try:
            network = ipaddress.ip_network(config.subnet, strict=False)
            alive_hosts = []

            with ThreadPoolExecutor(max_workers=self.network_cfg['max_workers']) as executor:
                futures = {
                    executor.submit(self._check_host, str(ip), config.ip): ip
                    for ip in network.hosts()
                }
                for future in as_completed(futures):
                    if result := future.result():
                        alive_hosts.append(result)

            self._save_results(config.interface, alive_hosts)
        except Exception as e:
            print(f"扫描 {config.interface} 失败: {str(e)}")

    def _check_host(self, ip: str, self_ip: str) -> Optional[str]:
        """检查单个主机"""
        if ip == self_ip:
            return None
        return ip if self._host_discovery(ip) else None

    def _host_discovery(self, ip: str) -> bool:
        """主机发现方法路由"""
        method = self.network_cfg['scan_method'].lower()
        if method == 'arp':
            return self._arp_ping(ip)
        elif method == 'icmp':
            return self._icmp_ping(ip)
        else:
            try:
                return ipaddress.ip_address(ip).is_private and self._arp_ping(ip) or self._icmp_ping(ip)
            except ValueError:
                return self._icmp_ping(ip)

    def _arp_ping(self, ip: str) -> bool:
        """ARP扫描实现"""
        try:
            pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
            resp = srp1(pkt, timeout=1, verbose=0)
            return resp is not None
        except Exception as e:
            if self.network_cfg['debug_mode']:
                print(f"ARP请求失败: {str(e)}")
            return False

    def _icmp_ping(self, ip: str) -> bool:
        """ICMP Ping实现"""
        params = {
            'timeout': self.network_cfg['ping_timeout'],
            'stdout': subprocess.DEVNULL,
            'stderr': subprocess.DEVNULL
        }
        cmd = ['ping', '-c', '1', '-W', str(self.network_cfg['ping_timeout']), ip] \
            if platform.system() != 'Windows' else \
            ['ping', '-n', '1', '-w', str(self.network_cfg['ping_timeout'] * 1000), ip]
        try:
            return subprocess.run(cmd, **params).returncode == 0
        except Exception as e:
            if self.network_cfg['debug_mode']:
                print(f"Ping失败: {str(e)}")
            return False

    def _save_results(self, interface: str, hosts: List[str]):
        """修正后的保存结果方法"""
        output_cfg = self.config_loader.get_output_config()
        filename = output_cfg['log_dir'] / f"{output_cfg['file_prefix']}{interface}.log"
        try:
            with open(filename, 'w') as f:
                f.write("\n".join(hosts) + "\n")
            print(f"{interface}: 发现 {len(hosts)} 台主机，结果保存至 {filename}")
        except IOError as e:
            print(f"保存失败: {str(e)}")


if __name__ == "__main__":
    try:
        scanner = NetworkScanner()
        configs = scanner.get_network_configs()

        if not configs:
            print("无有效网络接口")
            sys.exit(0)

        with ThreadPoolExecutor() as executor:
            executor.map(scanner.scan_network, configs.values())

    except Exception as e:
        print(f"运行错误: {str(e)}")
        sys.exit(1)