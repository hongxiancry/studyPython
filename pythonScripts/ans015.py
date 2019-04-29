
'''纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}'''
__author__='chairuiya'

import os,json
from xlwt import *
file = Workbook(encoding='utf-8')
table = file.add_sheet('city')

os.chdir('forans015')
cityTexts = ''
with open('city.txt','r') as cityText:
	cityTexts = cityText.read()
print(cityTexts)
cityContent = json.loads(cityTexts)
cityNum = list(cityContent.keys())
allcity = []
for i in range(len(cityNum)):
	tempcityvalue = []
	tempcityvalue.append(cityNum[i])
	tempcityvalue.append(cityContent[cityNum[i]])
	allcity.append(tempcityvalue)
print(allcity)

for row,citycontents in enumerate(allcity):
	valuelist = citycontents
	for column,cityInfo in enumerate(valuelist):
		table.write(row,column,cityInfo)
file.save('city.xls')
