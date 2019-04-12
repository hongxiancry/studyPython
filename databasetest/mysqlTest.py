import mysql.connector
connt = mysql.connector.connect(user='root',password='password',database='mysql_test')
cursor = connt.cursor()
cursor.execute(' create table if not exists scores (id varchar(20),name varchar(20),score int)')
cursor.execute('insert into scores (id,name,score) values(\'10\',\'lucy\',78)')
cursor.execute('insert into scores (id,name,score) values(\'11\',\'lili\',89)')
cursor.execute('insert into scores (id,name,score) values(\'12\',\'lili\',90)')

connt.commit()
cursor.close()
#查询操作
cursor = connt.cursor()
cursor.execute('select * from scores where score>=%s',(89,))
values = cursor.fetchall()
print("values:",values)
cursor.close()
connt.close()
