#函数式编程
#map的用法
from functools import reduce
def f(number):
	return number*number
numbers = [1,2,3,4,5,6]
m = map(f,numbers)
print("list m:",list(m))

strs = map(str,range(10))
print('strlist:',list(strs))
#filter的用法
def is_odd(n):
	return n%2==1
f = filter(is_odd,numbers)
print('filter f:',list(f))
#
def multiply(x,y):
	return x*y
re = reduce(multiply,numbers)
print('reduce: ',re)

