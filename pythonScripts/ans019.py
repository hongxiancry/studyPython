#__utf-8__
'''
将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下

所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!--
	数字信息
-->

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]

</numbers>
</root>
'''
'''
step1:read xls内容
step2:解析excel中读到的数据
step3:保存文件到制定位置
'''
__author__='chairuiya'

import xlrd
from xml.dom import minidom
import os,json

def readnumbers(path):
	excelData = xlrd.open_workbook(path)
	numbersInfo = excelData.sheet_by_name('numbers')
	return numbersInfo

def parseNumbers(sheet):
	strnumList = '['+'\n'
	for row in range(sheet.nrows):
		numbers = []
		for cols in range(sheet.ncols):
			numbers.append(int(sheet.cell(row,cols).value))
		strnumList += '      '+str(numbers)+','+'\n'
	strnumList+='    ]'
	print(strnumList)
	return strnumList

def saveNumToXML(path,numList):
	#创建xml文档对象
	xml = minidom.Document()
	xml.toxml(encoding='UTF-8')
	#创建根节点
	root = xml.createElement('root')
	#创建numbers节点
	numbers = xml.createElement('numbers')
	num_comment = xml.createComment(u'{space} 数字信息 {space}'.format(space = os.linesep))
	num_text = xml.createTextNode(numList)
	numbers.appendChild(num_comment)
	numbers.appendChild(num_text)
	root.appendChild(numbers)
	xml.appendChild(root)
	#格式化写入xml文件
	with open(path,'w') as file:
		xml.writexml(file,addindent='  ',newl='\n',encoding='utf-8')


		
#test_main
if __name__ == '__main__':
	os.chdir('forans016')
	numbersInfo = readnumbers('numbers.xls')
	numlist = parseNumbers(numbersInfo)
	saveNumToXML('numbers.xml',numlist)

