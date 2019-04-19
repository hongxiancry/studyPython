#每日一脚本
'第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。'
__author__='chairuiya'

import re
import collections
from collections import Counter

def statisticWords(file_path):
	with open(file_path,'r') as f:
		words = f.read()
		if words:
			mathces = re.findall(r'[\w\_\-]+',words)
			counts = collections.Counter(mathces)
			return counts	
		else:
			return 0
def staticWordsFormatPrint(counts):
	i=0
	for key in counts:
		i = i+1
		print('result2 %s:'%i,'%s:'%(key,),counts[key])
#测试程序
if __name__=='__main__':
	test_file_path = 'test0004.txt'
	testcounts = statisticWords(test_file_path)
	staticWordsFormatPrint(testcounts)
