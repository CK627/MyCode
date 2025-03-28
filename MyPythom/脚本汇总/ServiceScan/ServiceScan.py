import sys
import F1

if len(sys.argv)!=4:
    print('Usage:PortScan <IP> <port1> <port2>\n eg:ServiceScan 192.168.1.1 20 80')
    F2   //异常退出

target_ip=sys.argv[1]
target_port1=sys.argv[2]
target_port2=sys.argv[3]

nm=F1.F3
nm.scan(target_ip, F4+"-"+F5, "F6")
for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        lport=nm[host][proto].F7
        for port in lport:
            print('port:%s\tservice:%s' %(port, nm[host][proto][F8]['F9']))