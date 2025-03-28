#!/bin/python
import nmap
import sys
import threading

reload(sys)
sys.setdefaultencoding('utf-8')

def iphelp():
    print 'Usage: python os_scan.py ip'
    print '''ip format:
             singleip: 192.168.113.1
             rangeip:192.168.113.1-10
             wholenetwork:192.168.113.0/24
    ''' 

def inputipcheck(host):
    ip = host.split('.')
    if len(ip)!=4:
        return False
    else:
        return True

def ipcheck(host):
    ip = host.split('.')
    rep = []
    if '-' in ip[3]:
        rep1 = ip[3].split('-')
        rep2 = xrange(int(rep1[0]),int(rep1[1])+1)
        return rep2
    elif '/' in ip[3]:
        rep3 = xrange(1,255)
        return rep3
    else:
        rep.append(ip[3])
        return rep

def osscan(host, portrange):
    packet = nmap.PortScanner()
    pp = packet.scan(hosts=host, arguments='-O', ports=portrange, sudo=True)
    try:
        osinformation = ''.join(pp['scan'][host]['osmatch'][
                                0]['osclass'][0]['cpe'])
        osinformation = osinformation.split(':')
        osinformation = osinformation[2] + '/' + \
            osinformation[3] + ':' + osinformation[4]
        print 'The ip address is %s and operating system is %s' % (pp['scan'][host]['addresses']['ipv4'], osinformation)
    except (KeyError,IndexError),e:
        pass
        #print 'ip address: '+ host +' can not scan anything'

def docacle(host, portrange='80'):
    threadcounts = ipcheck(host)
    threads = []
    for i in threadcounts:
        iphost = host.split('.')
        ipaddress = iphost[0]+'.'+iphost[1]+'.'+iphost[2]+'.'+str(i)
        t = threading.Thread(target=osscan,args=(ipaddress,portrange,))
        threads.append(t)
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()
def main():
    if len(sys.argv) < 2:
        iphelp()
        print len(sys.argv)
    if inputipcheck(sys.argv[1]):
        docacle(sys.argv[1])
    else:
        iphelp()


if __name__ == '__main__':
    main()
