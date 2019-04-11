import os,sqlite3
db_file = os.path.join(os.path.dirname(__file__),'test.db')
print(db_file)
if os.path.isfile(db_file):
	os.remove(db_file)
try:
	connt = sqlite3.connect('test.db')
	cursor = connt.cursor()
	cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
	cursor.execute('insert into user (id,name) values(\'1\',\'cry\')')
	cursor.execute('alter table user add password varchar(20)')
	cursor.execute('insert into user (id,name,password) values(\'2\',\'maicel\',\'12345\')')
	count = cursor.rowcount
	print("rowcount:",count)
except:
	print("except found!")
finally:
	cursor.close()
	connt.commit()
	connt.close()

connt = sqlite3.connect('test.db')
cursor = connt.cursor()
cursor.execute('select * from user where id=?','2')
values = cursor.fetchall()
print('values:',values)
cursor.close()
connt.close()


