from scapy.all import *
import optparse
from threading import *
#flag1 = F1.F2.F3
def sweep(packet):
	try:
		reply = srp1(packet,timeout=1,verbose=0, iface='eth1') # 设置参数
		print('IP:',reply.psrc,'MAC:',reply.hwsrc) # 输出IP和MAC
	except:
		pass
#flag2 = F4.F5.F6
def main():
	parser = optparse.OptionParser('usage: -H <target host segment/eg:(192.168.0.)>')#设定-H参数
	parser.add_option('-H',dest='tgtHost',type='string',help='target host')#核心句
	(options,args) = parser.parse_args() # 同时设置两个变量
	host = options.tgtHost # 拿取tgtHost中的数据
	if host == None: # 如果没有，就提示
		print(parser.usage)
		exit(0) # 正常退出
	# 构建数据包
	eth = Ether()
	eth.dst = 'ff:ff:ff:ff:ff:ff'
	eth.type = 0x0806
	arp = ARP()
#flag3 = F7.F8.F9
#flag4 = F10.F11.F12
	# 线程攻击
	for n in range (254):
		arp.pdst = host + str(n)
		packet = eth/arp
		t = Thread(target=sweep,args=(packet)) #
		t.start()
#flag = F13.F14.F15
