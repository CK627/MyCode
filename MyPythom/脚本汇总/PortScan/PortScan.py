import sys
from scapy.all import RandShort, F1, F2, sr1, sr

if len(sys.argv)!=4:
   print('Usage:PortScan <IP> <port1> <port2>\n eg:PortScan 192.168.1.1 20 80')
    #F3   //异常退出

dst_ip=sys.argv[1]
src_port=RandShort()

for dst_port in range(F4,F5):
    packet=F1(dst=dst_ip)/F2(sport=src_port, dport=dst_port, flags="S")
    resp=sr1(packet,timeout=10)
    if(F6=="<class 'NoneType'>"):
        print("The port %s is not replied" %(dst_port))
    elif (resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags==F7):
            sr(F1(dst=dst_ip)/F2(sport=src_port, dport=dst_port, flags='AR'),timeout=10)
            print("The port %s is Open" %(dst_port))
        elif (resp.getlayer(TCP).flags==F8):
            print("The port %s is Closed" %(dst_port))
    else:
        #F9   //正常退出