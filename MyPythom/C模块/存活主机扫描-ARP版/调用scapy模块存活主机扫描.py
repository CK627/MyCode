from scapy.all import *

def arp(ip):
	try:
		packet=Ether(dst='FF:FF:FF:FF:FF:FF')/ARP(op=1,hwdst='00:00:00:00:00:00',pdst=ip)	
		result=srp(packet,timeout=0.1,iface='eth1',verbose=False)
		res=result[0].res
		if res != []:
			print ip,'is open'
	except:
		pass

if __name__ == '__main__':
	for i in range(254):
		ip='192.168.1.'+str(i)
		arp(ip)
