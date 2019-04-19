#utf-8
'你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。'

__author__='chairuiya'



import os,re
import answer004
from collections import Counter 


 #answer004.statisticWords(test_file_path)

def statisticKeyWords(test_dir_path):
	ifileCounters = Counter()
	for ifile in os.listdir(test_dir_path):
		#print('ifile:',ifile)
		filepath = os.path.splitext(ifile)
		if filepath[1]=='.txt':
			ifileCounters +=answer004.statisticWords(ifile)
		else:
			pass	
	return ifileCounters	
		

def findKeywords(ifileCounters,notKeywords):
	#过滤掉非关键词
	for nky in notKeywords:
		ifileCounters[nky]=0
	#Counters 根据关键词值排序
	listResult= sorted(ifileCounters.items(),key=lambda x:x[1],reverse=True)
	keyWordsList = listResult[0]
	#返回最多关键词的单词
	for i in range(len(listResult)):
		if int(listResult[i][1])>=int(keyWordsList[1]):
			keyWordsList+=listResult[i]
		else:
			pass
	return keyWordsList

			
#:test_main
if __name__=='__main__':
	currentdir = os.getcwd()
	test_dir_path = os.path.join(currentdir,'forans006')
	#print('dir:',test_dir_path)
	os.chdir(test_dir_path)
	testifileCounter = statisticKeyWords(test_dir_path)
	#print('testfile::',testifileCounter)
	notKeywords = ['I','we','he','his','her','she','the', 'in', 'of', 'and', 'to', 'has', 'that', 's', 'is', 'are', 'a', 'with', 'as', 'an']
	keyWordsList = findKeywords(testifileCounter,notKeywords)
	print('keywordsResult:',keyWordsList)