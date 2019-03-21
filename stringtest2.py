import math
import cmath
global str
n = 123
f = 456.789
s1 = 'Hello,world'
s2 = 'Hello,\'Adam\''
s3 = r'Hello, "Bart" '
s4 = '''Hello,
Lisa!'''
print(n,f,s1,s2,s3,s4)
print('class 3 ........\n')
ord('A')
chr(66)
'\u4e2d\u6587'
x=b'ABC'
print(x)
x1='Python-中文测试'
print(x1)
x2 = x1.encode('utf-8')
print('x2:',x2)
x3 = x2.decode('utf-8')
print('x3:',x3)
print('中文测试')
print('格式化练习%s')
s = 'Hello,%s' % 'name'
s5 = 'hi，%s,i have been got $%d' %('mary',1000000)
print(s5)
m1 = 72
m2 = 85
rr = (85-71)/71*100
s6 = '{0:.1f}%'.format(rr)
print(s6)
a=r'Hello\world\ls' '\\'
print(a)
a1 = u'zhongguollll'
print(a1)
print(abs(-2003))
m1 = math.sqrt(64)
print('m1:',m1)
#str1=input("hello:")
#print("input: "+str1)
n1 = int(84.89)
print(n1)
n2= 89903
print(n2)
n3 = math.ceil(89.3)
n4 = math.floor(87.6)
print("上位：",n3)
print('下位：',n4)
n5= pow(3,5,8)
print('奇怪数：',n5)
#str2 = input('raw_input:')
#print('raw input:'+str2)
r1 = round(2.33,1)
print('r1:',r1)
n2= str('abc')
print('str to number:',n2)
n3 = cmath.sqrt(-1)
print('out put cmath sqrt: ',n3)
#s = repr("hello,world")
print(repr("Hello,world"))
L1 = 100000000000000000000000
print(repr(L1))
print(str("Hello,wold,str"))


