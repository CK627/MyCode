#!/usr/bin/python
import sys
for i in range(10):
	try:
		r=sys.argv[i]
		print ord(r),
	except:
		continue
	
