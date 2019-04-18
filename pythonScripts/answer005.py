'第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率(1136x640)的大小。（遇到的问题，from PIL import Image 放在最前面，否则运行时会报错）'
__author__='chairuiya'

from PIL import Image
import os
import glob



#python 对文件和文件夹的操作
#获取当前目录



def thumbnailPics(imagesPath):
	imPath = glob.glob('*.jpeg')
	for imp in imPath:
		iPath = os.path.join(imagesPath,imp)
		im = Image.open(iPath)
		#print(im.format, im.size, im.mode)
		im.thumbnail((1136,640))
		#print(im.format, im.size, im.mode)
		im.save(iPath,'JPEG')
	print('just done!')

if __name__ == '__main__':
	currentPath = os.getcwd()
	#print('currentPath:',currentPath)
	imagesPath = os.path.join(currentPath,'foranswer005') 
	#print('imagesPath:',imagesPath)
	os.chdir(imagesPath)
	thumbnailPics(imagesPath)






