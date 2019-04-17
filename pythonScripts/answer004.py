#每日一脚本
'第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。'
__author__='chairuiya'

import re
import collections
from collections import Counter

def statisticWords(file_path):
	f  = open(file_path,'r')
	words = f.read()
	if words:
		mathces = re.findall(r'[\w\_\-]+',words)
		for countWords in mathces:
			counts = collections.Counter(mathces)
			count = (counts,countWords)[0]
			i = 0
			for key in count:
				i = i+1
				print('%s:'%(i,),'%s:'%(key,),count[key])
			return counts,countWords
	else:
		return (0,0)
if __name__=='__main__':
	test_file_path = 'test0004.txt'
	testcounts = statisticWords(test_file_path)