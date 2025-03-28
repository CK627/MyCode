import F1
import optparse

#Flag1 = F1

def osscan(host,port):
	try:
		a = nmap.PortScanner()
		F2 = a.scan(hosts=host,ports=port,arguments='-F3')
		print(((results['scan']['%s' % hostip]['osmatch'])[0])['name'])
	except: 
		pass
#Flag2 = F2
#Flag3 = F3
#Flag4 = F4

def main():
	parser = optparse.OptionParser('usage%prog'+'-H <target host>'+'-P <target>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-P', dest='tgtPort', type='string', help='specify target port')
	(options,args) = parser.parse_args()
	host = options.tgtHost
	port = options.tgtPort
	if host == None or port == None:
		print(parser.usage)
		exit(0)
	F5(host,port)

#Flag5 = F5

if __name__ == '__main__':
	main()
