import PySimpleGUI as sg
import socket
import struct
import random
import ipaddress
import platform
import sys
import subprocess
import os
import re
import ctypes
from threading import Thread
from netifaces import interfaces as net_ifaces


# DHCP报文生成模块
class DHCPGenerator:
    @staticmethod
    def generate_dhcp_discover(client_mac, xid=None, options=None):
        """生成DHCP Discover报文"""
        xid = xid if xid else random.randint(0, 0xFFFFFFFF)
        client_mac = [int(b, 16) for b in client_mac.split(':')]

        bootp = struct.pack('!4B', 0x01, 0x01, 0x06, 0x00)
        bootp += struct.pack('!L', xid)
        bootp += struct.pack('!HH', 0, 0)
        bootp += struct.pack('!4L', 0, 0, 0, 0)
        bootp += struct.pack('!6B', *client_mac) + b'\x00' * 10
        bootp += b'\x00' * 64 + b'\x00' * 128

        dhcp_options = bytes([
            0x63, 0x82, 0x53, 0x63, 0x35, 0x01, 0x01,
            0x3d, 0x06, *client_mac,
            0x37, 0x04, 0x01, 0x03, 0x06, 0x2a, 0xff
        ])

        return bootp + dhcp_options


# 跨平台网络工具
class NetworkUtils:
    @staticmethod
    def get_interfaces():
        system = platform.system()
        try:
            if system == "Darwin":
                return NetworkUtils._get_mac_interfaces()
            elif system == "Linux":
                return net_ifaces()
            elif system == "Windows":
                return NetworkUtils._get_windows_interfaces()
            return []
        except Exception as e:
            print(f"[ERROR] {str(e)}")
            return []

    @staticmethod
    def _get_mac_interfaces():
        try:
            output = subprocess.check_output(
                ["networksetup", "-listallhardwareports"],
                stderr=subprocess.STDOUT,
                timeout=5
            ).decode('utf-8')
            return [
                line.split(": ")[1]
                for line in output.split('\n')
                if "Hardware Port:" in line
            ]
        except Exception as e:
            print(f"[macOS ERROR] {str(e)}")
            return []

    @staticmethod
    def _get_windows_interfaces():
        try:
            import winreg
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"SYSTEM\CurrentControlSet\Control\Network\{4D36E972-E325-11CE-BFC1-08002BE10318}"
            )
            interfaces = []
            for i in range(winreg.QueryInfoKey(key)[0]):
                try:
                    guid = winreg.EnumKey(key, i)
                    subkey = winreg.OpenKey(key, f"{guid}\\Connection")
                    name = winreg.QueryValueEx(subkey, "Name")[0]
                    interfaces.append(name)
                except:
                    continue
            return interfaces
        except Exception as e:
            print(f"[Windows ERROR] {str(e)}")
            return []

    @staticmethod
    def check_root():
        if platform.system() == "Windows":
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        else:
            return os.getuid() == 0

    @staticmethod
    def bind_interface(sock, interface):
        system = platform.system()
        try:
            if system == "Linux":
                if interface and hasattr(socket, 'SO_BINDTODEVICE'):
                    sock.setsockopt(
                        socket.SOL_SOCKET,
                        socket.SO_BINDTODEVICE,
                        interface.encode()[:15]
                    )
            elif system == "Windows":
                import winreg
                key = winreg.OpenKey(
                    winreg.HKEY_LOCAL_MACHINE,
                    r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces"
                )
                ip_addr = None
                for i in range(winreg.QueryInfoKey(key)[0]):
                    guid = winreg.EnumKey(key, i)
                    subkey = winreg.OpenKey(key, f"{guid}")
                    try:
                        name = winreg.QueryValueEx(subkey, "Name")[0]
                        if name == interface:
                            ip_addr = winreg.QueryValueEx(subkey, "DhcpIPAddress")[0]
                            break
                    except:
                        continue
                if ip_addr:
                    sock.bind((ip_addr, 68))
            elif system == "Darwin":
                libc = ctypes.CDLL("libc.dylib")
                if_index = ctypes.c_uint32()
                libc.if_nametoindex(interface.encode(), ctypes.byref(if_index))
                sock.setsockopt(
                    socket.IPPROTO_IP,
                    0x21,
                    if_index
                )
        except Exception as e:
            print(f"接口绑定失败: {str(e)}")


class DHCPSender:
    def __init__(self):
        self.running = False
        self._check_permissions()
        self.window = self._create_gui()

    def _check_permissions(self):
        if not NetworkUtils.check_root():
            sg.popup_error("需要管理员权限运行！\n"
                           "Windows: 右键使用管理员身份运行\n"
                           "macOS/Linux: 使用sudo执行",
                           title="权限错误")
            sys.exit(1)

    def _create_gui(self):
        sg.theme('LightBlue2')

        layout = [
            [sg.Text("网络接口:", size=(10, 1)),
             sg.Combo([], key='-INTERFACE-', size=(30, 1)),
             sg.Button('刷新接口', key='-REFRESH-')],

            [sg.Frame('广播设置', [
                [sg.Radio('全网广播 (255.255.255.255)', "RADIO1", default=True, key='-GLOBAL-'),
                 sg.Radio('指定网段', "RADIO1", key='-CIDR-'),
                 sg.InputText('192.168.1.0/24', size=(15, 1), key='-CIDR_INPUT-')]
            ])],

            [sg.Frame('客户端参数', [
                [sg.Text("MAC地址:", size=(10, 1)),
                 sg.InputText(self._random_mac(), key='-MAC-', size=(20, 1)),
                 sg.Button('随机生成', key='-RAND_MAC-')]
            ])],

            [sg.HSeparator()],

            [sg.Button('发送单次请求', key='-SEND-'),
             sg.Button('开始压力测试', key='-STRESS-'),
             sg.Button('停止', key='-STOP-', disabled=True),
             sg.Exit()],

            [sg.StatusBar("就绪", key='-STATUS-', size=(60, 1), relief=sg.RELIEF_SUNKEN)]
        ]

        window = sg.Window("DHCP测试工具 v5.0", layout, finalize=True)
        self._refresh_interfaces(window)
        return window

    def _random_mac(self):
        return ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))

    def _refresh_interfaces(self, window):
        interfaces = NetworkUtils.get_interfaces()
        window['-INTERFACE-'].update(values=interfaces)
        if interfaces:
            window['-INTERFACE-'].update(value=interfaces[0])

    def _validate_input(self, values):
        if not re.match(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", values['-MAC-']):
            return False, "MAC地址格式错误"

        if values['-CIDR-']:
            try:
                network = ipaddress.IPv4Network(values['-CIDR_INPUT-'], strict=False)
                if network.prefixlen == 32:
                    return False, "CIDR格式错误"
            except:
                return False, "无效的网络地址"

        return True, ""

    def run(self):
        while True:
            event, values = self.window.read(timeout=100)

            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            if event == '-REFRESH-':
                self._refresh_interfaces(self.window)

            if event == '-RAND_MAC-':
                self.window['-MAC-'].update(self._random_mac())

            if event == '-SEND-':
                valid, msg = self._validate_input(values)
                if not valid:
                    sg.popup_error(msg)
                    continue
                Thread(target=self.send_packet, args=(values,), daemon=True).start()

            if event == '-STRESS-':
                self.running = True
                self.window['-STRESS-'].update(disabled=True)
                self.window['-STOP-'].update(disabled=False)
                Thread(target=self.stress_test, args=(values,), daemon=True).start()

            if event == '-STOP-':
                self.running = False
                self.window['-STRESS-'].update(disabled=False)
                self.window['-STOP-'].update(disabled=True)

            if event == '-STATUS_UPDATE-':
                self.window['-STATUS-'].update(values[event][0], text_color=values[event][1])

        self.window.close()

    def send_packet(self, values):
        try:
            iface = values['-INTERFACE-']
            client_mac = values['-MAC-']
            target_ip = '255.255.255.255' if values['-GLOBAL-'] else str(
                ipaddress.IPv4Network(values['-CIDR_INPUT-'], strict=False).broadcast_address
            )

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

            if iface:
                NetworkUtils.bind_interface(sock, iface)
            else:
                sock.bind(('0.0.0.0', 68))

            dhcp_packet = DHCPGenerator.generate_dhcp_discover(client_mac)
            sock.sendto(dhcp_packet, (target_ip, 67))
            self.window.write_event_value(('-STATUS_UPDATE-', (f"成功发送到 {target_ip}", 'green')), None)
        except Exception as e:
            self.window.write_event_value(('-STATUS_UPDATE-', (f"错误: {str(e)}", 'red')), None)
        finally:
            if 'sock' in locals():
                sock.close()

    def stress_test(self, values):
        count = 0
        while self.running:
            try:
                self.send_packet(values)
                count += 1
                self.window.write_event_value(
                    ('-STATUS_UPDATE-', (f"已发送 {count} 个请求", 'blue')), None)
            except Exception as e:
                self.window.write_event_value(
                    ('-STATUS_UPDATE-', (f"压力测试错误: {str(e)}", 'red')), None)
                break

if __name__ == "__main__":
    try:
        import netifaces
    except ImportError:
        sg.popup_error("需要安装netifaces库：pip install netifaces")
        sys.exit(1)

    if platform.system() == "Windows":
        import winreg
        from ctypes import windll

    DHCPSender().run()