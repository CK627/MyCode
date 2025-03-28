import socket  
  
def retBanner(ip,port):  
    try:  
        socket.setdefaulttimeout(2)  
        s = socket.socket()  
        s.connect((ip,port))  
        banner = s.recv(1024)  
        return banner  
    except:  
        return  
  
def checkVulns(banner):  
    if 'Serv-U' in banner:  
        print '[+] Microsoft IIS FTP is vulnerable.'   
    else:  
        print '[-] FTP Server is not vulnerable.'  
    return  
  
def main():  
	port = 21
	for i in range(1,254):
		try:
			ip='10.30.75.'+str(i)
			banner = retBanner(ip,port)  
			if banner:  
				print '[+] ' + ip + ':' + str(port) + '--' + banner  
			if port == 21:  
				checkVulns(banner)  
		except:
			print ip,'err'
  
if __name__ == '__main__':  
    main() 