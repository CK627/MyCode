from F1.all import *
import F2
from F3 import *

#flag1 = F1.F2.F3

def F4(packet):
	try:
		reply = srp1(packet,timeout=1,verbose=0, iface='eth1')
		print('IP:'+ reply.F5+'MAC:'+reply.F6)
	except:
		pass

#flag2 = F4.F5.F6

def main():
	parser = optparse.OptionParser('usage: -H <target host segment/eg:(192.168.0.)>')
	F7.add_option('-H',dest='tgtHost',type='string',help='target host')
	(F8,args) = parser.parse_args()
	F9 = options.tgtHost
	if host == None:
		print(parser.usage)
		exit(0)
	eth = F10()
	eth.F11 = 'ff:ff:ff:ff:ff:ff'
	eth.F12 = 0x0806
	arp = ARP()

#flag3 = F7.F8.F9
#flag4 = F10.F11.F12

	for n in range (254):
		arp.F13 = host + str(n)
		F14 = eth/arp
		F15 = Thread(target=sweep,args=(packet))
		t.start()
#flag = F13.F14.F15
