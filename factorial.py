#阶乘
def factorial(n):
	result = n
	for i in range(1,n):
		result*=i
	return result
print('result:',factorial(10))

def factorials(n):
	if n==1:
		return 1
	else:
		return n * factorials(n-1)
print('result:',factorials(10))
#幂的运算
def power(x,n):
	result = 1
	for i in range(n):
		result*=x
	return result
print('result power:',power(4,3))
def power(x,n):
	if n==0:
		return 1
	else:
		return x*power(x,n-1)
print('result power:',power(4,3))
#二分查找
def search(sequence,number,lower=0,upper=None):
	if upper is None:
		upper = len(sequence)-1
	if lower==upper:
		assert number==sequence[upper]
		return upper
	else:
		middle = (lower+upper)//2
		if number >sequence[middle]:
			lower = middle+1
			return search(sequence,number,lower,upper)
		else:
			return search(sequence,number,lower,middle)
sequence = [34,35,37,39,49,50]
i = search(sequence,39,0)
print('result i:',i)


