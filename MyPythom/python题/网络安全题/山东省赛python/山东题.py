# -*- codeing = utf-8 -*-
# 时间:2021/11/29 19:29
# 作者:CK
# 文件名:山东题.py
# 开发环境:PyCharm
import socket#导入socket这个模块

def a():#自定义一个函数

    for b in range(1,1023):#扫描端口范围1~1022
        c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#实例化一个socket对象
        c.settimeout(0.1)  # 设置超时时间，超过0.1秒钟还不能建立连接，就放弃这个端口号

        try:#尝试
            c.connect(('192.168.48.130',b))#输入端口，和端口
            print('已开放的端口：%d'%b)#打印

        except:#捕获异常数据
            pass#数据异常就跳过

zt()#调用此函数
'原理：利用TCP的三次握手，如果连接成功,这判定为端口开放'