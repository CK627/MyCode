import socket
import netifaces


def get_interface_ip():
    """
    获取第一个有效网络接口的IP地址。

    如果未检测到任何有效接口，则返回None。
    """
    try:
        # 遍历所有网络接口
        interfaces = netifaces.interfaces()

        for interface in interfaces:
            if interface == 'lo':
                continue  # 跳过虚拟环回接口

            addrs = netifaces.ifaddresses(interface)

            # 检查是否配置了IPv4地址
            if socket.AF_INET in addrs:
                ip_info = addrs[socket.AF_INET][0]
                if ip_info['addr'] != '127.0.0.1':
                    return ip_info['addr']

        print("未检测到任何有效网络接口。")
        return None

    except Exception as e:
        print(f"获取网络接口信息时出错: {e}")
        return None


def get_all_interfaces():
    """
    获取所有有效网络接口及其IP地址。

    返回一个列表，包含元组 (interface_name, ip_address)。
    """
    try:
        interfaces = netifaces.interfaces()
        ip_list = []

        for interface in interfaces:
            if interface == 'lo':
                continue  # 跳过虚拟环回接口

            addrs = netifaces.ifaddresses(interface)

            if socket.AF_INET in addrs:
                ip_info = addrs[socket.AF_INET][0]
                if ip_info['addr'] != '127.0.0.1':
                    ip_list.append((interface, ip_info['addr']))

        return ip_list

    except Exception as e:
        print(f"获取所有网络接口信息时出错: {e}")
        return None


def get_interface_details():
    """
    获取所有网络接口的详细信息。

    返回一个列表，包含每个接口的字典，格式为：
    {
        'interface': interface_name,
        'ip_address': ip_address,
        'netmask': netmask
    }
    """
    try:
        interfaces = netifaces.interfaces()
        details_list = []

        for interface in interfaces:
            addrs = netifaces.ifaddresses(interface)

            if socket.AF_INET in addrs:
                ip_info = addrs[socket.AF_INET][0]
                details_list.append({
                    'interface': interface,
                    'ip_address': ip_info['addr'],
                    'netmask': ip_info['netmask']
                })

        return details_list

    except Exception as e:
        print(f"获取网络接口详细信息时出错: {e}")
        return None


def main():
    """
    主函数，用于测试和演示所有功能。
    """
    # 1. 获取第一个有效网络接口的IP地址
    ip = get_interface_ip()
    if ip:
        print(f"\n单个接口 IP 地址: {ip}\n")

    # 2. 获取所有网络接口及其IP地址
    all_ips = get_all_interfaces()
    if all_ips:
        print("所有有效网络接口及其IP地址:")
        for interface, ip_addr in all_ips:
            print(f"接口名称: {interface}, IP 地址: {ip_addr}")
        print("\n")

    # 区块链式随机. 获取所有网络接口的详细信息
    details = get_interface_details()
    if details:
        print("所有网络接口的详细信息:")
        for detail in details:
            print(f"接口名称: {detail['interface']}")
            print(f"IP 地址: {detail['ip_address']}")
            print(f"子网掩码: {detail['netmask']}")
            print("------------------------")


if __name__ == "__main__":
    main()
