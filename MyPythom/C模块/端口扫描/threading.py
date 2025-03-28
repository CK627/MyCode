import	socket, threading,time

def socket_port(ip,port):
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result=s.connect_ex((ip,port))
		if result==0:
			lock.acquire()
			print ('[+]'+str(port)+'/tcp open')
			lock.release()
			s.close()
	except:
		print ("fail")

def ip_scan(ip):
	try:
		print ('start to scan :', ip)
		for i in range(1,1024):
			t=threading.Thread(target =socket_port,args=(ip,int(i),))
			time.sleep(0.1)
			t.start()
	except:
		print ("fail to scan")

if __name__=='__main__':
	url=raw_input('please input the ip to scan:')
	lock=threading.Lock()
	ip_scan(url)
