class FooBar:
	def __init__(self,value=90):
		self.somevar=value
f = FooBar()
print(f.somevar)
f1 = FooBar('HELLO')
print(f1.somevar)

class A:
	def hello(self):
		print('I\'m a')
class B(A):
	def hello(self):
		print('I\'m B')
a = A()
b = B()
a.hello()
b.hello()
#旧版的超类
class Bird:
	def __init__(self):
		self.hungry= True
	def eat(self):
		if self.hungry:
			print('eeee')
			self.hungry=False
		else:
			print('no,thanks')
class SingBird(Bird):
	def __init__(self):
		Bird.__init__(self)
		self.sound='adkg'
	def sing(self):
		print(self.sound)
bird = Bird()
bird.eat()
bird.eat()
sb = SingBird()
sb.sing()
sb.eat()
sb.eat()
#新版超类调用
__metaclass__ =type
class Bird:
	def __init__(self):
		self.hungry= True
	def eat(self):
		if self.hungry:
			print('eeee!!!')
			self.hungry=False
		else:
			print('no,thanks!!!')

class SingBird(Bird):
	def __init__(self):
		super(SingBird,self).__init__()
		self.sound='adkgoh!!'
	def sing(self):
		print(self.sound)
bird = Bird()
bird.eat()
bird.eat()
sb = SingBird()
sb.sing()
sb.eat()
sb.eat()
#成员访问：
def checkIndex(key):
	if not isinstance(key,(int)):raise TypeError
	if key<0:raise IndexError
class Abcd:
	def __init__(self,start=0,step=1):
		self.start = start
		self.step = step
		self.changed = {}
	def __getitem__(self,key):
		checkIndex(key)
		try:
			return self.changed[key]
		except:
			return self.start+key*self.step
	def __setitem__(self,key,value):
		checkIndex(key)
		self.changed[key] = value
	def __delitem__(self,key):
		del self.changed[key]
		
s = Abcd(1,2)
result= s[4]
print(result)
s[4]=2
result = s[4]
print(s[4])
del s[4]

#属性
class Rectangle:
	def __init__(self):
		self.width = 0
		self.height = 0
	def setSize(self,size):
		self.width,self.height = size
	def getSize(self):
		return self.width,self.height
	sizes = property(getSize,setSize)
r = Rectangle()
r.width = 10
r.height = 5
print(r.getSize())
r.setSize((100,120))
print(r.getSize())
print(r.width)
print(r.height)
print("property getSize:",r.sizes)
r.sizes = (150,100)
print("property restartSize:",r.sizes)

#装饰器
__metaclass__ = type
class Myclass:
	@staticmethod
	def smeth():
		print("smeth:::")
	@classmethod
	def cmeth(cls):
		print("cmeth:::",cls)
Myclass.smeth()
Myclass.cmeth()
#迭代器

it = iter([4,2,3])
for i in it:
	print(i)
it = [4,2,3]
for i in it:
	print(i)

#生成器
def flattern(nested):
	for sublist in nested:
		for num in sublist:
			yield num
nested = [[1,34,4],[8,9],[11]]
print(list(flattern(nested)))
#递归生成器
def flatternl(nested):
	try:
		for sublist in nested:
			for num in flattern(sublist):
				yield num
	except:
		print('something wrong')
		yield nested

nested = [[[1],2],3,4,[5,[6,7]],[8]]
print(list(flatternl(nested)))



