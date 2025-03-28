import psutil
import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_local_ip_addresses():
    addresses = {}
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                addresses[interface] = addr.address
    return addresses

def get_gateways():
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
    try:
        socket.create_connection((ip, 1399), timeout=0.3)
        return True
    except (socket.timeout, OSError):
        return False

def scan_ip(ip, interface, local_ip, gateways):
    ip_str = str(ip)
    if ip_str == local_ip or ip_str in gateways:
        return None
    if is_host_alive(ip_str):
        return ip_str
    return None

def scan_network(interface, base_ip, local_ip, gateways):
    subnet = ipaddress.ip_network(f"{base_ip}/24", strict=False)
    alive_hosts = []
    print(f"开始扫描网卡 {interface} 的网段 {subnet}...")
    with ThreadPoolExecutor(max_workers=50) as executor:
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
    return alive_hosts

def save_results(interface, hosts, base_file_path="scan_results"):
    if hosts:
        file_path = f"{interface}.log"
        with open(file_path, "w") as file:
            file.write("\n".join(hosts))
        print(f"网卡 {interface} 的扫描日志已保存到 {file_path}")
    else:
        no_alive_hosts_log = "no_alive_hosts.log"
        with open(no_alive_hosts_log, "a") as file:  # 使用追加模式
            file.write(f"网卡 {interface} 未发现存活主机\n")
        print(f"网卡 {interface} 未发现存活主机，已记录到 {no_alive_hosts_log}")

def main():
    local_ips = get_local_ip_addresses()
    if not local_ips:
        print("未检测到网卡和对应的 IP 地址。")
        return
    gateways = get_gateways()
    print("检测到的网卡和 IP 地址:")
    for interface, ip in local_ips.items():
        print(f"{interface}: {ip}")
    with ThreadPoolExecutor(max_workers=len(local_ips)) as executor:
        future_to_interface = {
            executor.submit(scan_network, interface, ip, local_ips[interface], gateways): interface
            for interface, ip in local_ips.items()
        }

        for future in as_completed(future_to_interface):
            interface = future_to_interface[future]
            try:
                alive_hosts = future.result()
                save_results(interface, alive_hosts)
            except Exception as e:
                print(f"{interface} 扫描时出现错误: {e}")

if __name__ == "__main__":
    main()