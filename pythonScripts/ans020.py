#--coding utf-8 --
'''
第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，
点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日
通话详单.xls 文件。写代码，对每月通话时间做个统计。
'''

import xlrd
import os

def countTelTimes(path):
	excelData = xlrd.open_workbook(path)
	sheet = excelData.sheet_by_index(0)
	total_time = 0
	for row in range(1,sheet.nrows):
		total_time += int(sheet.cell(row,3).value)
	return total_time

#test_main
if __name__ == '__main__':
	os.chdir('forans020')
	total_time=countTelTimes('teleinfo.xls')
	total_minutes = total_time/60
	print('通话时长总共%.2f分钟'%(total_minutes))




