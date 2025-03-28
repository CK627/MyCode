import subprocess

for i in range(20,26):
	ip='192.168.44.'+str(i)		
	list=['7000','7001','7002']
	print ip
	for port in list:
		try:
			subprocess.call(['nc',ip,port,'-w 1'])
		except:
			pass
