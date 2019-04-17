#每日一脚本
'第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。'
__author__='chairuiya'

import re


def statisticWords(file_path):
	f  = open(file_path,'r')
	words = f.read()
	if words:
		mathces = re.findall(r'[\w\_\-\;\,\.]+',words)
		return mathces
	else:
		return 0
if __name__=='__main__':
	test_file_path = 'test0004.txt'
	testwords = statisticWords(test_file_path)
	i = 0;
	for testword in testwords:
		i = i+1
		print('%s:'%(i,),testword)