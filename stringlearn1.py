#第三章练习1
#字符串是不可变的
import math
from string import Template 
#from string import maketrans


website = 'http://www.python.org'
ws = list(website)
print(ws)
ws[-3:] = 'com'
print('ws:',ws)
wst = ''.join(ws)
print('wst:',wst)


format = "Hello,%s.%s enough for you?"
values = ('world','lili')
print(format%values)

format = 'Pi with three decimals:%.3f'
print(format%math.pi)
s = Template('$x, gorlg $x')
print('s: ',s.substitute({'x':'abc'}))
s = Template('x,gong${x}')
print('s: ',s.substitute({'x':'he'}))
s= Template('x,$$30 abcd $x')
print('s: ',s.substitute({'x':'efg'}))
s = Template('A $thing must never $action')
d = {}
d['thing'] = 'gentlemen'
d['action'] = 'show is socks'
print('s: ',s.substitute(d))
print('%s plus %s equals %s'%(1,3,4))
print('%10.1f'%math.pi)
print('%-*s%*s'%(15,'abcd dieg',10,'34555'))
width = int(input('please input width:'))
price_width = 10
item_width = int(width-price_width)
heard_format = '%-*s%*s'
content_format = '%-*s%*.2f'
print('='*width)
print(heard_format%(item_width,'Item',price_width,'Price'))
print('-'*width)
print(content_format%(item_width,'Apple',price_width,0.4))
print(content_format%(item_width,'Pears',price_width,1.5))
print('='*width)

#字符串的方法
worlds = 'find my name'
s1 = worlds.find('find')
print('s1: ',s1)
s2 = worlds.find('name')
print('s2: ',s2)
s3 = worlds.find('abc')
print('s3: ',s3)

n1 = ['1','2','3']
ntos = '+'.join(n1)
print('ntos: ',ntos)

lowerstr = 'abcdefg'
upperstr = lowerstr.upper()
print(upperstr)

replaceworlds = 'this is a small test'
print('replaceworlds:',replaceworlds.replace('this','it'))

splitstr = '1+2+3+4+9'.split('+')
print('splitstr: ',splitstr)
stripstr = '   women   is  gold    '
stripstr1 = stripstr.strip()
print("stripstr: ",stripstr)
print('stripstr1:',stripstr1)

table =''.maketrans('cs','kz')
worlds = 'this is an incredible test'
print('translate: ',worlds.translate(table))







