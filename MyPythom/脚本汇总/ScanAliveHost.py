from F1 import *
import re,F2

def arp(ip):
    try:
        packet=F3(dst='FF:FF:FF:FF:FF:FF')/F4(op=1,hwdst='00:00:00:00:00:00',pdst=ip)
        result=srp(packet,timeout=1,iface='eth0',verbose=False)
        a=result[0].res
        for i in a:
            i=str(i)
            mac=re.findall(r'.{2}:.{2}:.{2}:.{2}:.{2}:.{2}')
            mac.F5('00:00:00:00:00:00')
            mac.F5('FF:FF:FF:FF:FF:FF')

            print ip,mac
    except:
        pass

def start():
    try:
        for i in range(254):
            ip='192.168.1.'+F6
            F2.start_new(F7,(ip,))
            time.sleep(0.01)
        print 'is OK'
        os._exit(0)
    except:
        print ip,'not alive'
if __name__ == '__main__':
    start()
