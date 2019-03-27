#第六章抽象
'''
#test1
import math
fibs = [0,1]
for i in range(8):
	fibs.append(fibs[-2]+fibs[-1])
print(fibs)
#test2
fibs = [0,1]
num = int(input('How many Fibonacci numbers do you want?'))
for i  in range(num-2):
		fibs.append(fibs[-2]+fibs[-1])
print(fibs)
#test3
x = 1
y = math.sqrt
print('call x:',callable(x))
print('call y:',callable(y))
def hello(name):
	print('hello:'+name+'!')
hello('world')
#test4
def fibs(num):
	result = [0,1]
	for i in range(num-2):
	    result.append(result[-2]+result[-1])
	return result
fibs = fibs(5)
print(fibs)
'''
#test5 文档化函数

def square(x):
	'''calculates the square of the number x''' 
	return x*x
x = square(4)
print('square x:',x)
#help(square)

#返回值为空
def test():
	print('this is printed.')
	return
	print('this is not printed.')
x = test()
print('x:',x)
#函数对值的作用
def try_to_changename(name):
	name = 'abc'
n = 'mr.li'
try_to_changename(n)
print('n:',n)

def try_to_changenames(names):
	names[0]='abc'
namest = ['mer','cde']
print('before namest:',namest)
try_to_changenames(namest)
print('after namest:',namest)

def init(data):
	data['first'] = {}
	data['middle'] = {}
	data['last'] = {}
storage = {}
init(storage)
#print('storage:',storage)

def lookup(data,label,name):
	return data[label].get(name)
def store(data,full_name):
	names = full_name.split(' ')
	if(len(names))==2:
		names.insert(1,'')
	print('names: ',names)
	labels = ['first','middle','last']
	for label,name in zip(labels,names):
		people = lookup(data,label,name)
		if people:
		#	print('people:',people)
			people.append(full_name)
		#	print('append after people:',people)
		else:
			data[label][name] = [full_name]
	#print('data:',data)

mynames = {}
init(mynames)
store(mynames,'jim asd facts')
store(mynames,'jim asd set')
store(mynames,'jim asd facts')
#关键字参数和默认值
def hello(name='lisa',greeting='hello'):
	print(greeting,name,'!')
hello('xiaoyang')
hello()
hello(greeting='nihao')
#收集参数
def print_params(*params):
	print(params)
print_params('test1','test2')
#练习使用参数
def interval(start,stop=None,step=1):
	if stop is None:
		start,stop=0,start
	result = []
	i = start
	while i < stop:
		result.append(i)
		i+=step
	return result

print(interval(10))
print(interval(10,15,2))

x=1
scope = vars()
print(scope['x'])
scope['x']+=5
print(scope['x'])
print('x:',x)
abc=int('1')
def try_tochange():
	global abc
	abc = abc+1
print('abc: ',abc)

def multiplier(factor):
	def multiplyByFactor(number):
		return number*factor
	return multiplyByFactor
double = multiplier(3)
print('double:',double(5))
result = multiplier(5)(6)
print('result:',result)











