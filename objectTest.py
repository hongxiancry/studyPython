#多态的练习
#函数的多态
def length_message(x):
	print('The length of',repr(x),'is',len(x))
length_message('30')
length_message([1,3,5])
def add(x,y):
	return x+y
print(add('a','b'))
print(add(3,4))
#对象的多态
print('aabc'.count('a'))
print([1,2,'a'].count('a'))


#封装
class Book:
	def setBookName(self,name):
		self.name = name
	def getName(self):
		return self.name
	def showName(self):
		print('This book\'s name is %s'%self.name)
b1 = Book()
b2 = Book()
b1.setBookName('python learning')
b2.setBookName('python3 learning')
b1.showName()
b2.showName()
name= b1.getName()
print(name)
#特性、函数、方法
class Secretive:
	def __inaccessive(self):
		print('bet you can not see this function')
	def accessive(self):
		print('The secret is :')
		self.__inaccessive()
se = Secretive()
se.accessive()
se._Secretive__inaccessive()
#类的命名空间
def foo(x):
	return x*x
foo1 = lambda x:x*x
r1= foo(2)
print('r1:',r1)
r2 = foo1(3)
print('r2:',r2)

class MemberCounter:
	memberNum = 0
	def init(self):
		MemberCounter.memberNum+=1
m1 = MemberCounter()
m1.init()
print(MemberCounter.memberNum)
m2 = MemberCounter()
m2.init()
print(MemberCounter.memberNum)
#子类和超类
class Filter():
	def init(self):
		self.blocked = []
	def filter(self,sequence):
		return [x for x in sequence if x not in self.blocked]
class SubFilter(Filter):
	def init(self):
		self.blocked = ['sub']
f = Filter()
f.init()
l = f.filter([1,2,3])
print('result l:',l)
subF = SubFilter()
subF.init()
subL = subF.filter(['sub','eggs','meig'])
print('resultsubl:',subL)
print(issubclass(SubFilter,Filter))

#多类
class Calculator:
	def calculate(self,expression):
		self.value = eval(expression)
class Talker:
	def talk(self):
		print('calculate result is : ',self.value)
class TalkingCalculator(Calculator,Talker):
	pass
talkcal = TalkingCalculator();
talkcal.calculate('1*10+8*7')
talkcal.talk()



