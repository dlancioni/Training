import os
import psycopg2

os.system("cls")

cn = psycopg2.connect(host='tuffi.db.elephantsql.com', 
                      database='qqbzxiqr',
                      user='qqbzxiqr', 
                      password='EmiJvVhFJGxDEKJoV6yK9A6o2G5pkmR9')

cursor = cn.cursor()

cursor.execute("select 1 as Id, 'David' as Name")

result = cursor.fetchall()

for x in result:
  print(x[1])
  
cn.close()  