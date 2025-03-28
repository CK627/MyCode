# -*- coding = utf-8 -*-
# @Time:2023/2/16 8:44
# @Author:CK
# @File:服务端
# @Software:PyCharm
import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#实例化一个socket对象；参数AF_INET表示socket网络层使用IP协议;参数SOCK_STREAN表示该socket传输层使用tcp协议
server.bind(('0.0.0.0',800))#主机地址为0.0.0.0，表示所有不清楚的主机和目的网络。
server.listen(5)
print(f'服务端启动成功，在{800}端口等待客户连接.....')
dataSocket, add = server.accept()
print("接受一个客户连接：",add)

def handle_sock(sock,addr):
    while True:
        data = sock.recv(1024)
        print('接受对方消息：',data.decode('utf-8'))
        re_date = input('>>')
        if re_date=='0':
            break

        sock.send(re_date.encode('utf-8'))
#获取从客户端发送的数据
#一次获取1k的数据
while True:
    sock, addr = server.accept()
    #用线程去处理新接受的连接（用户）
    client_therad=threading.Thread(target=handle_sock,args=(sock,addr))
    client_therad.start()