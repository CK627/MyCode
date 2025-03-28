import os,time,subprocess
for i in range(254):
	target="192.168.1."+str(i)
	try:
		subprocess.call(['arping',target])
	except:
		print 'bad target'
		
