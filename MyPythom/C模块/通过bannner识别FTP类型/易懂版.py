import socket

def ftp(ip,port):
	try:
		socket.setdefaulttimeout(0.1)
		s=socket.socket()
		s.connect((ip,port))
		banner=s.recv(1024)
		check(banner)
	except:
		pass

def check(banner):
	if "vsFTPd" in banner:
		print 'is vsftpd'
	else:
		print 'is not vsftpd'

def main():
	port = 21
	for i in range(1,254):
		ip = "192.168.44."+str(i)
		print ip
		ftp(str(ip),port)

if __name__ == '__main__':
	main()
