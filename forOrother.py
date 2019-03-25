#条件循环&其他语句

from math import sqrt as foobar

print(foobar(4))
#赋值魔法
x,y,z = 1,2,3
print(x,y,z)
x,y = y,x
print(x,y,z)
values = 3,2,1
print('values: ',values)
x,y,z = values
print('x,y,z:',x,y,z)
scoundrel = {'name':'robin','girlfriend':'Marion'}
key,value= scoundrel.popitem()
print('key:',key)
print('value:',value)
x=2
x+=1
x*=2
print('x:',x)
fnord = 'foo'
fnord+= 'bar'
fnord*=2
print('fnord: ',fnord)
print(bool('42'))
print(bool(''))
print(bool(0))
print(bool(None))
print(bool({}))
print(bool('abc'))

num = input('Enter a number: ')
num = int(num)
if num > 0:
	print('The number is positive')
elif num < 0:
	print('The number is negative')
else:
	print('The number is zero')
name = input('input your name:')
if name.endswith('Gumby'):
	if name.startswith('Mr.'):
		print('hello,Mr')
	elif name.startswith('Mrs.'):
		print('hello,Mrs')
	else:
		print('oh,hi')
	
else:
	print('hi')
x = y =[1,2,3]
z = [1,2,3]
print(x is y)
print(x==y)
print(x==z)
print(x is z)
x = [1,2,3]
y = [2,4]
print(x is not y)
del x[2]
y[1]  = 1
y.reverse()
print(x==y)
print(x is y)

name = input('input your name:')
if 's' in name:
	print('Your name contains the letter \'s\'')
else:
	print('Your name does not contain the letter \'s\'')
	
number = input('Enter a number between 1 and 10：')
number = int(number)
if number<=10:
	if number>=1:
		print('Great!')
	else:
		print('number shoule be >=1')
else:
	print('number should be <=10')
if number<=10 and number>=1:
	print('Great!')
elif number<1:
	print('number shoule be>=1')
elif number>10:
	print('number should be<=10')
	
#循环
name = ''
while not name:
	name = input('please input your name:')
print('hello,%s !'%name)

words = ['adke','dfe','dett','pouu']
for word in words:
	print(word+'\n')
	
d = {'a':'1','b':'2','c':'3'}
for key in d:
     print(key,'=',d[key])
for key,value in d.items():
	print(key,'=',value)

name = ['anna','lli','susi']
ages = ['12','14','11']
for i in range(len(name)):
	print(name[i],'age is ',ages[i])
infos = zip(name,ages)
for na,age in infos:
	print(na,'age is ',age,'years old')
#迭代工具
strings = ['3','333kkd','m']
for index,string in enumerate(strings):
	print(index,':',string)
	if '3' in string:
		strings[index] = '[censored]'
		print('index:',index)

num = input('please input number: ')
num = int(num)
for i in range(0,10,2):
	if num==i:
		print(i)
		break
while True:
	word = input('please input your name:')
	if not word:
		break
	print('word:',word)
	

print([x*x for x in range(10) if x%2==0])
print([(x,y) for x in range(3) for y in range(4)])

girls = ['alice','bernic','clarice']
boys = ['chirs','arnold','bob']
lettergirls = {}
for girl in girls:
	lettergirls.setdefault(girl[0],[]).append(girl)
	print(lettergirls)
print([b+'+'+g for b in boys for g in lettergirls[b[0]]])


exec("print('hello,world')")
eval(input('enter a program:'))
scope = {}
scope['x'] = 2
scope['y'] = 3
eval('x*y',scope)

