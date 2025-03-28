# -*- coding = utf-8 -*-
# @Time:2022/12/6 14:14
# @Author:CK
# @File:批量端口扫描Windows版
# @Software:PyCharm
import threading # 导入threading库
from socket import * # 导入socket库
from alive_progress import alive_bar # 导入 alive-progress 库
import os # 导入内置库os



lock = threading.Lock()  # 确保多个线程在共享资源的时候不会出现脏数据
threads = []  # 创建一个列表，在这里表示线程池，用于存放多个线程，可存放的线程数由电脑性能决定
a = [] # 创建一个列表，在这里用来存放开放的端口


def One_port_scan(host, port): # 自定义一个函数
    try: # 尝试运行
        s = socket(AF_INET, SOCK_STREAM) # 创建一个socket
        s.connect((host, port)) # 连接主机和对应的端口，
        lock.acquire() # 锁定线程，防止在运行此线程的时候运行其他线程。
        a.append(f"{port}") # 在列表的末尾添加port这个变量里面的值
        lock.release() # 解锁线程，让其他线程可运行
        s.close() # 关闭连接
    except: # 如果运行失败则
        pass # python内置函数，意思是跳过


def Port_scanning_of_one_IP(ip, ports=range(65535)):  # 自定义函数 设置 端口缺省值0-65535，端口不写默认到65535
    setdefaulttimeout(0.1) # 设置超时时间
    for port in ports: # 循环端口
        t = threading.Thread(target=One_port_scan, args=(ip, port)) # 创建线程
        threads.append(t) # 讲线程添加到线程池的末尾
        t.start() # 运行线程
    for t in threads: # 循环遍历线程池
        t.join() # 用于守护子线程，只有当使用了join的函数的线程运行结束了才会结束代码


data = [] # 创建一个列表，用于存储扫出的存活的靶机
def Survival_host_scanning():
    a, b, c, d = input("输入开始ip：").split(".")
    q, w, e, r = input("输入结束ip：").split(".")
    for i in range(int(a), int(q) + 1):
        for x in range(int(b), int(w) + 1):
            for l in range(int(c), int(e) + 1):
                for y in range(int(d), int(r) + 1):
                    wang = os.popen("ping -n 1 -w 1 " + str(i) + "." + str(x) + "." + str(l) + "." + str(y)).readlines()
                    ze = str(wang).find("TTL")
                    if ze >= 0:
                        data.append(str(i) + "." + str(x) + "." + str(l) + "." + str(y))
                    else:
                        print(str(i) + "." + str(x) + "." + str(l) + "." + str(y) + "\n login down")

    print("----------------------------------------------------------------------")
    if len(data) != 0:
        for i in data:
            print(i)
    else:
        print("检测范围内没有存活靶机")


def Port_scanning_for_multiple_IPs():
    global a # 声明a是全局变量
    Survival_host_scanning() # 调用函数，可以理解为运行此函数
    with open("dk.txt", "w+") as dk:  # 用with函数，可以防止忘记关闭文件时，所导致的文件读取异常
        ths = [] # 创建一个列表，在这里表示线程池，用于存放多个线程，可存放的线程数由电脑性能决定
        ks, js = input("请输入要扫描端口的范围（用“-”隔开）:").split("-") # 为变量赋值，每个变量用-隔开
        # 使用 with 语句创建一个进度条
        with alive_bar(len(data), force_tty=True) as bar:# 给 alive_bar 传入进度条总数目（这里是 列表data的长度）
            for i in data: # 循环存活靶机，方便每个IP创建线程
                d = threading.Thread(target=Port_scanning_of_one_IP(i.strip(), range(int(ks), int(js) + 1))) # 创建线程
                d.start()  # 启动线程
                ths.append(d) # 将线程加入到线程池中
                dk.write(i+":"+str(a)+"\n") # 写入文件
                a = [] # 清空存放开放端口的列表，防止出现上一个IP存活的端口，出现在下一个IP存活的端口
                bar() # 更新进度条
            for t in ths: # 循环遍历线程池

                t.join() # 守护子线程，只有当使用了join的函数的线程运行结束了才会结束代码


if __name__ == '__main__':
    Port_scanning_for_multiple_IPs()