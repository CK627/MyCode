import requests,time
while True:
	try:
		requests.get('http://192.168.1.55')
	except:
		print 'req down'

