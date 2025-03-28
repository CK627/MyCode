 from  scapy.all import  *
 def iCMP(i):
	ip=IP( )
	ip.src="172.16.101.%5"%i
	ip.dst 172.16.101.248"
	icmp=ICMP( )
	ether=Ether( )
	packet=ether/ip/icmp/"hello,world"
	sendp(packet)
while 1:
	for i in  range(1,254):
		iCMP( i)