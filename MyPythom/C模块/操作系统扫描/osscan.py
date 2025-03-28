import nmap
import optparse

def osscan(host):
	scanner = nmap.PortScanner()
	results = scanner.scan(hosts=host,arguments='-O')
	res = results['scan'].values()
	print res[0]['osmatch'][0]['name']

def main():
	parser=optparse.OptionParser('usage%prog'+'-H <target>')  #括号中的内容为帮助信息,"%prog"为文件名
	parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
	(options,args) = parser.parse_args()
	host=options.tgtHost   #获得的host是dest的值
	if host==None:
		print parser.usage   #当没有传入值时显示帮助
		exit(0)
	osscan(host)

if __name__ == '__main__':
	main()
