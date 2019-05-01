# -*- coding: utf-8 -*-

'''第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中。'''

import json,os
from xlwt import *
file = Workbook(encoding = 'utf-8')
table = file.add_sheet('student')

os.chdir('forans014')
with open('student.txt','r') as txtfile:
	filecontent = txtfile.read()
	#将str转换为dict
	pythonString = json.loads(filecontent)
	print('bef:',pythonString)
	#pythonString = sorted(pythonString.items(),key = lambda item:item[0])
	#print('aft:',pythonString)
	keys = list(pythonString.keys())
	values = list(pythonString.values())
	print(values)
	alldata = []
	for i in range(len(keys)):
		tempdata = []
		tempdata.append(keys[i])
		for j in range(len(values[i])):
			tempdata.append(values[i][j])
		alldata.append(tempdata)
	print(alldata)

	for row,key in enumerate(alldata):
		Valuelist = key
		for column,i in enumerate(Valuelist):
			print(i)
			table.write(row,column,i)

file.save('student.xls')

