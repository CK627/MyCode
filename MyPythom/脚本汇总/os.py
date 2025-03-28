import nmap
import optparse

def osscan(host,port):
	try:
		hostip = host
		print(hostip)
		a = nmap.PortScanner()
		results = a.scan(hosts=host,ports=port,arguments='-O')
		print(((results['scan']['%s' % hostip]['osmatch'])[0])['name'] )
	except: 
		pass

def main():
	parser = optparse.OptionParser('usage%prog'+'-H <target host>'+'-P <target>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-P', dest='tgtPort', type='string', help='specify target port')
	(options,args) = parser.parse_args()
	host = options.tgtHost
	port = options.tgtPort
	if host == None or port == None:
		print (parser.usage)
		exit(0)
	osscan(host,port)

if __name__ == '__main__':
	main()
