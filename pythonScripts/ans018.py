#'utf-8'
'''将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下 所示：

    <?xmlversion="1.0" encoding="UTF-8"?>
    <root>
    <cities>
    <!-- 
    	城市信息
    -->
    {
    	"1" : "上海",
    	"2" : "北京",
    	"3" : "成都"
    }
    </cities>
    </root>

}'''

'''
step1:read xls内容
step2:解析excel中读到的数据
step3:保存文件到制定位置
'''
__author__='chairuiya'

import xlrd
from collections import defaultdict
import os,json
from xml.dom import minidom
import codecs

def readxls(path):
	'''
	path xls文件路径
	return excelData数据
	'''
	excelData = xlrd.open_workbook(path)
	cityInfo = excelData.sheet_by_name('city')
	return cityInfo

def parseCityExeclInfo(sheet):
	'''
	sheet 待解析excel内容
	return strCityData可写入xml的字符串
	'''
	jsonData = defaultdict(list)
	for row in range(sheet.nrows):
		for cols in range(1,sheet.ncols):
			jsonData[sheet.cell(row,0).value].append(sheet.cell(row,cols).value)
	strCityData = str(json.dumps(jsonData,indent=4,ensure_ascii=False))
	return strCityData

def saveCityInfotoXML(path,cityInfo):
	#创建xml文档对象
	xml = minidom.Document()
	xml.toxml(encoding='UTF-8')
	#创建根节点：
	root = xml.createElement('root')
	#创建city节点
	cities = xml.createElement('cities')
	city_text = xml.createTextNode(cityInfo)
	city_comment = xml.createComment(u'{space} 城市信息 {space}'.format(space=os.linesep))
	cities.appendChild(city_comment)
	cities.appendChild(city_text)
	root.appendChild(cities)
	xml.appendChild(root)

	#格式化输出到xml中
	with codecs.open(path,'w',encoding='utf-8') as wbxml:
		allxmlData = xml.toprettyxml(indent='\t',encoding='utf-8')
		#print(type(allxmlData))
		allxmlData=str(allxmlData,encoding="utf-8").replace('&quot;','"')
		wbxml.write(allxmlData)


#test_main
if __name__ == '__main__':
	os.chdir('forans015')
	citySheet = readxls('city.xls')
	strCityData = parseCityExeclInfo(citySheet)
	#print(strCityData)
	saveCityInfotoXML('city.xml',strCityData)



