#list 练习

print(list('hello'))
x = [1,1,1]
print('before: ',x)
x[1] = 2
print('after: ',x)
del x[1]
print('del: ',x)
x[1:] = list('xyz')
print('cover:',x)
x[1:1] = [2,3,4]
print('cover:',x)
del x[1:4]
print('recover:',x)

lst = [1,2,3]
lst.append(5)
print(lst)
number = [5,6,7,9]
lst.append(number)
print('sencond lst:',lst)
print(lst.count(5))
lst.extend(number)
print('after extend lst:',lst)
number1 = ['s','h']
lst[len(lst):]=number1
print('after slice lst:',lst)
print(lst[4])
print('hahah:',lst)
lst.insert(2,'a')
print('insert :',lst)
lst.pop()
popstr=lst.pop(2)
print('pop string:',popstr)
print('pop:',lst)
lst.remove('s')
print('remove:',lst)
lst.reverse()
print('reverse: ',lst)
print('list :',list(lst))
sortlst = [1,3,9,4,5]
#sortlst.sort()
print('sort:',sortlst)
x = sortlst
y = x[:]
y.sort()
print('y: ',y)
print('x: ',x)
x1 = [2,4,1,3]
y1 = sorted(x1)
print('x1:',x1)
print('y1:',y1)
lst1 = sorted('stl')
print('lst1:',lst1)

#高级排序
def cmp(a,b):
	return (a>b)-(a<b)
cmp1 = cmp(34,45)
print(cmp1)
print(cmp(45,44))
print(cmp(44,44))
numbers = [5,2,9,7]
numbers.sort(reverse=True)
print('numbers:',numbers)
strs = ['3iei','ii','ieijg']
strs.sort(key=len)
print('strs: ',strs)

#元组
t = (1,2,3)
print('t: ',t)
t = (1,)
print('t:',t)
t = 3*(42,)
print('t: ',t)
x = 1,2,3
print('x:',x[1])
print('x:',x[0:2])
y = [3,4,5]
y = tuple(y)
print('y:',y)
