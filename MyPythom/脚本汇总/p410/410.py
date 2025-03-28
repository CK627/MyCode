import sys
from scapy.all import flag1 ,flag2 , sr1 , sr
if len(sys.argv) != 4:
    print('eg:PortScan 192.168.65.1 20 80')
    flag3 // 异常退出
for dst_port in range(flag4,flag5):
    dst_ip = sys.argv[1]
    resp = sr1(flag1(dst=dst_ip) / flag2(dport=dst_port, flags="S"), timeout=10)

    if flag6 == "<class 'NoneType'>":
        print("The port %s is Closed" % (dst_port))

    elif (resp.haslayer(TCP)):
        if (resp.getlayer(TCP).flags == flag7):
            flag10 = sr(flag1(dst=dst_ip) / flag2(dport=dst_port, flags="AR"), timeout=0.5, verbose=0)
            print("The port %s is open" % (dst_port))

        elif (resp.getlayer(TCP).flags == flag8):
            print("The port %s is Closed" % (dst_port))

flag9      // 正常退出


1