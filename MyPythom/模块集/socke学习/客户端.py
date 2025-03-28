# -*- coding = utf-8 -*-
# @Time:2023/2/16 8:44
# @Author:CK
# @File:客户端
# @Software:PyCharm
import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#实例化一个socket对象；参数AF_INET表示socket网络层使用IP协议;参数SOCK_STREAN表示该socket传输层使用tcp协议
client.connect(('127.0.0.1',10000))# 对方IP地址和端口
while True:
    re_date=input('输入-1退出对话>>')
    if re_date=='-1':
        break
    client.send(re_date.encode('utf-8'))
    data=client.recv(1024)#定义一次从socket缓冲区最多读入1k数据
    print('接受对方消息：',data.decode('utf-8'))