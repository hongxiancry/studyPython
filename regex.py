import re
print(re.search('na','no'))
print(re.match('...\w\we','centre').group())
print(re.search('i\s\S','juli Sing').group())
print(re.search('\w+c{2}\w*','aaccmmob\'s bar').group())
#abc-def@gmail.com
print(re.search(r'([\w.-]+)@([\w-]+).([\w]+)','please email to shijialong.study@gmail.com').group())

matchs= re.findall('advi[cs]e','I could advise you on your poem, but you would disparage my advice')
for m in matchs:
	print(m+'\n')
import os
filecwd = os.getcwd()
print(filecwd)
os.chdir(filecwd)
f = open('pythonRegx.txt')
match = re.findall('[\w]*python[\w]*',f.read())
for mw in match:
	print(mw)
match = re.findall(r'([\w]+)\s([\w]+)','abc dib,didng dkg,domie')
for i in match:
	print(i)
match = re.findall(r'</?\w+>','<em>abcd</em> <li>iekg</li>')
for i in match:
	print(i)
match = re.findall(r'(a*?)b','aaabb')
for i in match:
	print(i)
strs = 'a apple'
strs=re.sub('^a','an',strs)
print(strs)