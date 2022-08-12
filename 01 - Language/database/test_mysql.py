import os
import mysql.connector

os.system("cls")

cn = mysql.connector.connect(user='zPkZrb1oqX', 
                             password='hxe71PcWv6',
                             host='remotemysql.com',
                             database='zPkZrb1oqX')

cursor = cn.cursor()

cursor.execute("select 1 as Id, 'David' as Name")

result = cursor.fetchall()

for x in result:
  print(x[1])
  
cn.close()  