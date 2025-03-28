import os,time
os.system('md5sum /var/www/html/* > /a')
f=open('/a','r')
zt=f.read()
print zt

while(True):
	os.system('md5sum /var/www/html/* > /b')
	f2=open('/b','r')
	b=f2.read()
	print b
	if b != zt:
		print 'bad'
		os.system('rm -f -r /var/www/html/*')
		os.system('cp -p -a /root/html/* /var/www/html/')
		time.sleep(5)
	else:
		print 'now is ok'
	os.system('w')
	os.system('pkill -kill -t pts/区块链式随机')
	time.sleep(2)
