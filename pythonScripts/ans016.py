' 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：请将上述内容写到 numbers.xls 文件中'
'''
[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]'''
from xlwt import *
import os,json

file = Workbook(encoding='utf-8')
table = file.add_sheet('numbers')
os.chdir('forans016')

with open('numbers.txt') as myNumFile:
	myNums = myNumFile.read()
	myNum = json.loads(myNums)
	print(myNum)
	for i,num in enumerate(myNum):
		print(i,num)
		for j,values in enumerate(num):
			print(i,j,values)
			table.write(i,j,values)
file.save('numbers.xls')



