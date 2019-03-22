#字典
from copy import deepcopy

names = ['a','b','c']
numbers = ['1','2','3']
print(numbers[names.index('b')])
phonebox = {'a':'1','b':'2','c':'3'}
items = [('name','xiaoqiang'),('age',20)]
d = dict(items)
print('d:',d)
print('items:',items)

x = []
x.append('a')
print('x:',x)
x = {}
x[3]='lll'
x['name']='lili'
x['phoneno'] = '29030049'
print('key:map',x)
x.clear()
print('after clear x: ',x)

x = {'a':'1','b':'2','c':'3','d':['5','6']}
y = x.copy()
y['a']='4'
y['d'].remove('5')
print('x:',x)
print('y:',y)

m1= {'a':'1','b':'2','c':'3','d':['5','6']}
m2 = deepcopy(m1)
m2['a']='90'
m2['d'].remove('6')
print('m1: ',m1)
print('m2: ',m2)
print('get function: ',m1.get('a'))

dicts = dict.fromkeys(['name','age'])
dicts['name']='lisa'
dicts['age'] = 21
print('dict fromkeys:',dicts)

print('has_key:',dicts.get('abc'))

people = {'apple':{'phone':'29045','addr':'a'},'ooo':{'phone':'90395','addr':'c'}}
labels = {'phone':'phone number','addr':'address'}
name = input('please input your name:')
request = input('phone number(p) or address(a)?')
if request == 'p':key = 'phone'
if request == 'a':key = 'addr'
person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key,'not available')
print('%s\'s %s is  %s'%(name,label,result))

people = {'apple':{'phone':'29045','addr':'a'},'ooo':{'phone':'90395','addr':'c'}}
print(people.items())
people.pop('ooo')
print('pop people:',people)
people['ccc']={'phone':'29904','addr':'3o'}
print('people:',people)
print('popitem people',people.popitem())
print('people:',people)

people['sss']={'phone':'9304','addr':'8903'}
updates = {'sss':{'phone':'9899','addr':'98655'}}
print('before update people:',people)

people.update(updates)
print('after update people:',people)
print('people values: ',people.values())

