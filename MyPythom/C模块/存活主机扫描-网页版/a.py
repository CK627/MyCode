import requests
for i in range(254):
	try:
		requests.get("http://172.16.107."+str(i),timeout=0.0001)
		print (i)
	except:
		print(i,'bad url')
