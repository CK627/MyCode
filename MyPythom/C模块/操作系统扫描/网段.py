import nmap
import optparse

def osscan(host):
	try:
		scanner = nmap.PortScanner()
		results = scanner.scan(hosts=host,arguments='-O')
		res = results['scan'].values()
		ra= res[0]['osmatch'][0]['name']
		ra=host+' '+str(ra)
		lista.append(ra)
	except:
		pass

def main():
	for i in range(40):
		ip='172.16.101.'+str(i)
		osscan(ip)

if __name__ == '__main__':
	global lista
	lista=[]
	main()
	print lista
