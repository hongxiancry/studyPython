import os
dirname = os.getcwd()
os.chdir(dirname)

try:
	file = open('fileIOtest.txt','a')
	file.write('this is test file'+'\n'+'python IO'+'\n' 'include read and write!'+'\n'+'file over...'+'\n')
finally:
	file.close()

try:
	file = open('fileIOtest.txt','r')
	for line in file:
		print(line)
finally:
	file.close()
try:
	file = open('fileIOtest.txt')
	strs = file.readlines()
	print(strs)
finally:
	file.close()
try:
	file = open('fileIOtest.txt','r')
	i = int(0)
	while True:
		line = file.readline()
		if not line:
			break
		else:
			i=i+1
			print(i,':'+line)
finally:
	file.close()

with open('fileIOtest.txt') as line:
	print(line.readlines())

try:
	file = open('fileIOtest.txt','r')
	strss = file.read(5)
	print(strss)
finally:
	file.close()

