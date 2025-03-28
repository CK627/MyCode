#!/usr/bin/python
import os,time,subprocess
l=[]
old="'root','root'"		
old2='"root","root"'
for load,dirs,files in os.walk('/var/www/html/'):
	for zt in files:
		l.append(os.path.join(load, zt))

for i in l:
	f=open(i,'r+')
	for line in f:
		if old in line or old2 in line:
			print i
