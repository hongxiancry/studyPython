'将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如'
__author__='chairuiya'
'''
step1:读取xls的内容
step2:解析出文件内容
stpe3:将解析的内容插入xml文件中
'''

from lxml import etree
import xlrd
import os,json
import xml.etree.ElementTree as ET
from xml.dom import minidom
from collections import defaultdict


os.chdir('forans014')

def openxls(path):
	excelData = xlrd.open_workbook(path)
	studentInfo = excelData.sheet_by_name('student')
	return (studentInfo)

def bulidStudentsInfos(sheet):
	jsonData = defaultdict(list)
	for row in range(sheet.nrows):
		for cols in range(1,sheet.ncols):
			jsonData[sheet.cell(row,0).value].append(sheet.cell(row,cols).value)
	print(';;;;',jsonData)
	return jsonData


def saveInfotoXml(path,jsonData):
		root = ET.Element("root")
		comment = ET.Comment(u'{space}学生信息表{space} "id" :[名称，数学，语文，英文]{space}'.format(space=os.linesep))
		students = ET.SubElement(root,'students')
		students.insert(1,comment)
		students.text = str(json.dumps(jsonData,indent=4,ensure_ascii=False))
		print('text:',students.text)
		tree = ET.ElementTree(root)
		tree.write(path,encoding='utf-8',xml_declaration=True)




#test_main
if __name__ == '__main__':
	mytestInfo = openxls('student.xls')
	myjsonData = bulidStudentsInfos(mytestInfo)
	saveInfotoXml('student.xml',myjsonData)


