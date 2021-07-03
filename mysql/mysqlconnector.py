import MySQLdb
conn = MySQLdb.connect(host='172.16.67.22', user='root',passwd='936005485',db='test')
cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()
print "server version:",row[0]
cursor.close()
conn.close()