import psutil
import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_local_ip_addresses():
    """获取本地所有网卡的 IP 地址"""
    addresses = {}
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                addresses[interface] = addr.address
    return addresses

def get_gateways():
    """获取所有活动网卡的网关地址"""
    gateways = psutil.net_if_stats()
    gateway_ips = []
    for interface, stats in gateways.items():
        if stats.isup:
            gws = psutil.net_if_addrs().get(interface, [])
            for gw in gws:
                if gw.family == socket.AF_INET:
                    gateway_ips.append(gw.address)
    return gateway_ips

def is_host_alive(ip):
    """检查目标 IP 是否存活"""
    try:
        socket.create_connection((ip, 80), timeout=1)
        return True
    except (socket.timeout, OSError):
        return False

def scan_ip(ip, interface, local_ip, gateways):
    """扫描单个 IP 是否存活"""
    ip_str = str(ip)
    if ip_str == local_ip or ip_str in gateways:
        return None
    if is_host_alive(ip_str):
        return ip_str
    return None

def scan_network(interface, base_ip, local_ip, gateways):
    """扫描指定网段的所有 IP"""
    subnet = ipaddress.ip_network(f"{base_ip}/24", strict=False)
    alive_hosts = []
    print(f"开始扫描网卡 {interface} 的网段 {subnet}...")
    with ThreadPoolExecutor(max_workers=500) as executor:
        future_to_ip = {
            executor.submit(scan_ip, ip, interface, local_ip, gateways): ip
            for ip in subnet.hosts()
        }
        for future in as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                result = future.result()
                if result:
                    alive_hosts.append(result)
            except Exception as e:
                print(f"扫描 {ip} 时出错: {e}")
    return {interface: alive_hosts}

def save_results_to_files(results, base_file_path="scan_results"):
    """
    保存扫描结果：
    - 每个网卡单独生成一个日志文件
    - 未发现存活主机的网卡记录到一个集中日志中
    """
    no_alive_hosts_log = "no_alive_hosts.log"
    no_alive_hosts_interfaces = []

    for interface, hosts in results.items():
        if hosts:  # 有存活主机
            file_path = f"{interface}.log"
            with open(file_path, "w") as file:
                file.write("\n".join(hosts))
            print(f"网卡 {interface} 的扫描日志已保存到 {file_path}")
        else:  # 无存活主机
            no_alive_hosts_interfaces.append(interface)

    if no_alive_hosts_interfaces:
        with open(no_alive_hosts_log, "w") as file:
            file.write("以下网卡未发现存活主机:\n")
            file.write("\n".join(no_alive_hosts_interfaces))
        print(f"未发现存活主机的网卡已记录到 {no_alive_hosts_log}")

def main():
    local_ips = get_local_ip_addresses()
    if not local_ips:
        print("未检测到网卡和对应的IP地址。")
        return
    gateways = get_gateways()
    print("检测到的网关地址:", gateways)
    print("检测到的网卡和IP地址:")
    for interface, ip in local_ips.items():
        print(f"{interface}: {ip}")
    results = {}
    with ThreadPoolExecutor(max_workers=len(local_ips)) as executor:
        future_to_interface = {
            executor.submit(scan_network, interface, ip, local_ips[interface], gateways): interface
            for interface, ip in local_ips.items()
        }

        for future in as_completed(future_to_interface):
            interface = future_to_interface[future]
            try:
                result = future.result()
                results.update(result)
            except Exception as e:
                print(f"{interface} 扫描时出现错误: {e}")
    print("\n存活主机日志:")
    for interface, hosts in results.items():
        print(f"{interface}: {', '.join(hosts) if hosts else '无存活主机'}")
    save_results_to_files(results)

if __name__ == "__main__":
    main()