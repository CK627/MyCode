import psutil
import socket
import ipaddress
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_local_ip_and_subnets():
    interfaces = {}
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                ip = addr.address
                netmask = addr.netmask
                subnet = f"{ip}/{netmask_to_prefix(netmask) if netmask else 24}"
                interfaces[interface] = subnet
    return interfaces

def netmask_to_prefix(netmask):
    try:
        return sum(bin(int(octet)).count('1') for octet in netmask.split('.'))
    except AttributeError:
        return 24

def get_gateways():
    gateways = []
    for interface, stats in psutil.net_if_stats().items():
        if stats.isup:
            for addr in psutil.net_if_addrs().get(interface, []):
                if addr.family == socket.AF_INET:
                    gateways.append(addr.address)
    return gateways

def is_host_alive(ip):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Ping {ip} 出现异常: {e}")
        return False

def scan_ip(ip, local_ip, gateways):
    ip_str = str(ip)
    if ip_str == local_ip or ip_str in gateways:
        return None
    if is_host_alive(ip_str):
        return ip_str
    return None

def scan_network(interface, subnet, local_ip, gateways):
    network = ipaddress.ip_network(subnet, strict=False)
    print(f"开始扫描网卡 {interface} 的网段 {network}...")
    alive_hosts = []
    try:
        with ThreadPoolExecutor(max_workers=50) as executor:
            future_to_ip = {
                executor.submit(scan_ip, ip, local_ip, gateways): ip
                for ip in network.hosts()
            }
            for future in as_completed(future_to_ip):
                try:
                    result = future.result()
                    if result:
                        alive_hosts.append(result)
                except Exception as e:
                    print(f"扫描 {future_to_ip[future]} 时出错: {e}")
    except Exception as e:
        print(f"扫描网卡 {interface} 时出现异常: {e}")
    if alive_hosts:
        file_path = f"{interface}.log"
        try:
            with open(file_path, "w") as file:
                file.write("\n".join(alive_hosts) + "\n")
            print(f"网卡 {interface} 的扫描结果已保存到 {file_path}")
        except Exception as e:
            print(f"保存网卡 {interface} 的扫描结果时出错: {e}")
    else:
        print(f"网卡 {interface} 扫描完成，无存活主机。")

def main():
    interfaces = get_local_ip_and_subnets()
    if not interfaces:
        print("未检测到网卡和对应的IP地址。")
        return

    gateways = get_gateways()
    print("检测到的网关地址:", gateways)

    print("检测到的网卡及其网段:")
    for interface, subnet in interfaces.items():
        print(f"{interface}: {subnet}")

    with ThreadPoolExecutor(max_workers=len(interfaces)) as executor:
        future_to_interface = {
            executor.submit(scan_network, interface, subnet, subnet.split('/')[0], gateways): interface
            for interface, subnet in interfaces.items()
        }

        for future in as_completed(future_to_interface):
            interface = future_to_interface[future]
            try:
                future.result()
                print(f"网卡 {interface} 的扫描线程已完成。")
            except Exception as e:
                print(f"扫描网卡 {interface} 时出现错误: {e}")

if __name__ == "__main__":
    main()