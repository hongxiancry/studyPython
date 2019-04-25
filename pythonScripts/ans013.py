
'第 0013 题： 用 Python 写一个爬图片的程序，爬（http://tieba.baidu.com/p/2166231880'
__author__='chairuiya'

from PIL import Image
import requests
import re,os

def getHtmlImageInfo(requestUrl,saveDir):
	htmlData = requests.get(requestUrl).text
	urls = re.findall(r'src="(http://imgsrc.baidu.com/forum/.*?)"',htmlData,re.S)
	download_pic(urls,saveDir)

def download_pic(urls,downloadDir):
	countpic= 0
	if not os.path.exists(downloadDir):
		os.mkdir(downloadDir)
	else:
		os.chdir(downloadDir)
		for dwpic in urls:
			print(dwpic)
			pics = requests.get(dwpic)
			print('pics',pics)
			savePic = str(countpic)+'.jpg'
			print(savePic)
			with open(savePic,'wb') as fileWs:
				fileWs.write(pics.content)
			countpic = countpic+1
	print(countpic)


#test_download_pics
if __name__ == '__main__':
	downloadDir = 'forans013'
	requestUrl = 'http://tieba.baidu.com/p/2166231880'
	getHtmlImageInfo(requestUrl,downloadDir)
