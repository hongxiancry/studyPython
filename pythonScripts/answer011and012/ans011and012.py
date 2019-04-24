#__*__utf-8

__author__='chairuiya'

'第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。'
import re,os

def filterStopWords(userInputWords):
	with open('filtered_words.txt','r') as allstopWords:
		stopWords = allstopWords.read().split('\n')
		stopflag = False
		for stopWord in stopWords:
			if stopWord in userInputWords :
				stop_word_len = len(stopWord)
				userInputWords = userInputWords.replace(stopWord,'*'*stop_word_len)
				if not stopflag:
					print('Freedom')
					stopflag = True 
				else:
					pass
			else:
				if not stopflag:
					print('Human Rights')
				else:
					pass
		print('userInputWords:',userInputWords)

#test
if __name__ == '__main__':
	userInputWords = input('please input your search words:')
	filterStopWords(userInputWords)

