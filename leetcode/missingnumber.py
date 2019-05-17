#coding utf-8
__author__='chairuiya'
#leetcode 题目：给定一个包含0,1,2...n的序列，找出0.。n中没有出现序列中的那个数

#第一种方法 1
#0...n相加，减去给定的数组，得到的数就是没有出现的数
def missingNumber(args):
	n = len(args)
	sum = (n)*(n+1)//2
	for i in range(n):
		sum -=args[i]
	return sum



#第二种方法
#二分法查找
def missNumber_2(args):
	args.sort()
	print(args)
	n = len(args)
	left = 0
	right = n
	while left<right:
		mid = (left+right)//2
		if args[mid]>mid:
			print(args[mid],mid)
			right = mid
			print('right:',right)
		else:
			print(args[mid],mid)
			left = mid+1
			print('left:',left)
	return left

#第三种方法
#相与
def missNumber_3(args):
	n = len(args)
	res = 0
	for i in range(n):
		res = res^i^args[i]
		print('res:',res)
		i=i+1
	return res^i
	
def missNumber_4(args):
	n = len(args)
	res = n
	for i in range(n-1):
		i=i+1
		res = res^args[i]
		res = res^i
	return res



#test_main
if __name__ == '__main__':
	testargs = [0,1,4,5,3,7,2,8]
	num = missingNumber(testargs)
	print('the missing num is :',num)
	num2 = missNumber_2(testargs)
	print('the function2 find num:',num2)
	num3 = missNumber_3(testargs)
	print('the function3 find num:',num3)
	num4 = missNumber_4(testargs)
	print('the function4 find num:',num4)
