# -*- coding: utf-8 -*-
'第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。'
__author__='chairuiya'

import re,os,string

'''
多行注释1
多行注释2


多行注释3
多行注释4
'''

"""
多行注释5
多行注释6

多行注释7
多行注释8
"""

#统计行数函数：
def countlineNum(path):
	#注释的三种类型：1.’#‘开头的单行注释 2.’’‘’‘开头和结尾的多行注释 3。'"""'开头和结尾的多行注释
	#空行，strip之后==‘’
	#剩余为代码行
	codeLineNum = 0
	commentLineNum = [0,0]
	commentTotalNum = 0
	is_mulit_comment = False
	blankLineNum = 0
	totalNum = 0

	#打开文件
	with open(path,'r') as file:
		for f in file.readlines():
			totalNum+=1
			codes = f.strip()
			if codes=='' and not is_mulit_comment:
				blankLineNum+=1
			elif re.match('^#',codes):
				commentLineNum[0]+=1
			elif codes.startswith("'''") or codes.endswith("'''") or codes.startswith('"""') or codes.endswith('"""'):
				commentLineNum[1]+=1
				is_mulit_comment = not is_mulit_comment
			elif is_mulit_comment:
				commentLineNum[1]+=1
			else: 
				codeLineNum+=1
		commentTotalNum = commentLineNum[0]+commentLineNum[1]
	return (totalNum,codeLineNum,blankLineNum,commentTotalNum)

#计算目录下所有文件总的代码行数、空行、注释行
def dirCountLineNum(dirpath):
	dirfiles = os.listdir(dirpath)
	fileCountLine = (0,0,0,0)
	for dirfile in dirfiles:
		if os.path.isfile(dirfile):
			filepath = os.path.splitext(dirfile)
			if filepath[1] == '.py':
				tempCountNum = countlineNum(dirfile)
				fileCountLine = tuple(map(lambda x:x[0]+x[1],zip(fileCountLine,tempCountNum)))
				
		elif os.path.isdir(dirfile):
			dirCountLineNum(dirfile)
		else:
			pass
	return fileCountLine


#test_main
if __name__=='__main__':
	osdirpath = os.getcwd()
	#testpath = os.path.join('ans007.py')
	mytestLine = dirCountLineNum(osdirpath)
	print('''总代码数是：%s
代码数：%s
空行数：%s
注释行数：%s'''%(mytestLine[0],mytestLine[1],mytestLine[2],mytestLine[3]))