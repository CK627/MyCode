from scapy.all import *
import optparser
from threading import *

#flag1 = F1.F2.F3

def sweep(packet):
	try:
		reply = srp1(packet,timeout=1,verbose=0, iface='eth1')
		print 'IP:'+ reply.psrc+'MAC:'+reply.hwsrc
	except:
		pass

#flag2 = F4.F5.F6

def main():
	parser = optparse.OptionParser('usage: -H <target host segment/eg:(192.168.0.)>')
	parser.add_option('-H',dest='tgtHost',type='string',help='target host')
	(options,args) = parser.parse_args()
	host = options.tgtHost
	if host == None:
		print parser.usage
		exit(0)
	eth = Ether()
	eth.dst = 'ff:ff:ff:ff:ff:ff'
	eth.type = 0x0806
	arp = ARP()

#flag3 = F7.F8.F9
#flag4 = F10.F11.F12

	for n in range (254):
		arp.pdst = host + str(n)
		packet = eth/arp
		t = Thread(target=sweep,args=(packet))
		t.start()
#flag = F13.F14.F15
