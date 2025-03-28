from optparse import OptionParser
import nmap,os,re

def scan(host):
	nm = nmap.PortScanner()
	result=nm.scan(hosts=host,arguments='-O')
	os=re.findall(r'\[\'cpe:/o:(.{1,50})\'\]',str(result))
	print str(host)+':',os

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option('-H','--host',type='string',dest='host')
	(options,args)=parser.parse_args()
	host=str(options.host)
	if host == None:
		print 'please input host'
		os._exit(0)
	else:
		scan(host)
