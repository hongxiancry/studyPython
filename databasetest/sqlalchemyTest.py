from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base = declarative_base()

#定义对象
class User(Base):
	#表名字：
	__tablename__='user'


	#表结构：
	id = Column(String(20),primary_key=True)
	name = Column(String(20))

#初始化数据库连接：
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/mysql_test')
#括号中数据代表’数据库名+数据库驱动：//用户名：密码口令：机器地址/数据库名‘
DBseesion = sessionmaker(bind=engine)

#数据库中插入数据
session = DBseesion()
new_user = User(id='6',name='lili01')
session.add(new_user)
new_user1 = User(id='9',name='test02')
session.add(new_user1)
session.commit()
session.close()

#查询数据库中数据
session = DBseesion()
#创建查询，filter是where条件，最后调用.one()返回一行，.all()返回全部结果
user = session.query(User).filter(User.id>='5').all()
def print_result(users):
	for user in users:
		print(user.id)
		print(user.name)

print_result(user)
session.close()

