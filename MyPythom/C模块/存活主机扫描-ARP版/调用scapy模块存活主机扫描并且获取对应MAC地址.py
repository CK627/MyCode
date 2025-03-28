from scapy.all import *
import re,thread

def arp(ip):
	try:
		packet=Ether(dst='FF:FF:FF:FF:FF:FF')/ARP(op=1,hwdst='00:00:00:00:00:00',pdst=ip)	
		result=srp(packet,timeout=1,iface='eth1',verbose=False)
		a=result[0].res
		for i in a:
			i=str(i)
			mac=re.findall(r'.{2}:.{2}:.{2}:.{2}:.{2}:.{2}',i)
			mac=list(set(mac))
			mac.remove('00:00:00:00:00:00')
			mac.remove('FF:FF:FF:FF:FF:FF')
			print ip,mac
	except:
		print ip,'is bad'
def start():
	try:
		for i in range(254):
			ip='192.168.1.'+str(i)
			thread.start_new(arp,(ip,))	
			time.sleep(0.01)
		print 'is OK'
		os._exit(0)
	except:
		print ip,'not alive'
		

if __name__ == '__main__':
	start()
