#生成的二维码存储到mysql数据库中
#/Users/chairuiya/Documents/learn/studyPython/001
#_*_ utf-8 _*_
__author__ = 'chairuiya'

import mysql.connector
import answer001

connt = mysql.connector.connect(user='root',password='chai20190906',database='mysql_test')
cursor = connt.cursor()
cursor.execute('DROP TABLE IF EXISTS codes')
cursor.execute('create table codes (id varchar(20) primary key,codevalue varchar(20))')

codeLen = 10
codeCount = 200
for code in range(codeCount):
	codevalues = answer001.generateCode(1,codeLen)
	#print("codevalues:",codevalues)
	sqlinsert = """insert into codes (id,codevalue) values(%s,%s)"""
	cursor.execute(sqlinsert,[code+1,codevalues])

#事务提交插入数据库
connt.commit()
cursor.close()


#查询数据库
if __name__== '__main__':
	cursor = connt.cursor()
	cursor.execute('select * from codes')
	print ('codes results:',cursor.fetchall())
	cursor.close()
connt.close()