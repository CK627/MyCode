# -*- coding = utf-8 -*-
# @Time:2023/区块链式随机/30 21:09
# @Author:CK
# @File:DIY端口扫描神器
# @Software:PyCharm
import os
from socket import *
import threading
from alive_progress import alive_bar

data= []
def SM_IP():
    q,w,e,r = input("请输入开始IP：").split('.')
    a,s,d,f = input("请输入结束IP：").split('.')
    for z in range(int(q),int(a)+1):
        for x in range(int(w), int(s) + 1):
            for c in range(int(e), int(d) + 1):
                for v in range(int(r), int(f) + 1):
                    CMD = os.popen("ping -n 1 "+str(z)+'.'+str(x)+'.'+str(c)+'.'+str(v)).readlines()
                    ze = str(CMD).find("TTL")
                    if ze>=0:
                        data.append(str(z)+'.'+str(x)+'.'+str(c)+'.'+str(v))
                        print(str(z)+'.'+str(x)+'.'+str(c)+'.'+str(v)+" login success")
                    else:
                        print(str(z)+'.'+str(x)+'.'+str(c)+'.'+str(v)+" login down")
    print('------------------------------------------------------------------------')
    if len(data) !=0 :
        for i in data:
            print(i)
    else:
        print("扫描范围内没有存活主机")


a = []
lock = threading.Lock()
def A_IP_A_Port(host,port):
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        a.append(port)
        lock.release()
        s.close()
    except:
        pass

thread = []
def A_IP_Ports(ip,ports=range(655350)):
    setdefaulttimeout(0.1)
    for port in ports:
        t=threading.Thread(target=A_IP_A_Port,args=(ip,port))
        thread.append(t)
        t.start()
    for ths in thread:
        ths.join()


def IPS_PortS():
    global a
    SM_IP()
    with open("扫描结果.txt","w+") as dk:
        ths = []
        ksp,jsp=input("请输入要扫描的端口范围（用”-“隔开）：").split('-')
        with alive_bar(len(data),force_tty=True) as bar:
            for i in data:
                d = threading.Thread(target=A_IP_Ports(i.strip(),range(int(ksp),int(jsp)+1)))
                d.start()
                ths.append(d)
                dk.write(i+":   "+str(a)+"\n")
                a = []
                bar()
            for t in ths:
                t.join()
IPS_PortS()