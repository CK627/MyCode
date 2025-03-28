#!/usr/bin/python
import sys
for i in range(100):
	try:
		r=sys.argv[i]
		zt=int(r)
		print chr(zt),
	except:
		continue
	
