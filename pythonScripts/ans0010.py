
'第 0010 题：使用 Python 生成类似于图中的字母验证码图片'
__author__='chairuiya'

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import string

def genernateSecImage(secNum):

	#use a truetype font
	font = ImageFont.truetype("Arial.ttf",30)

	width = 80*4
	height = 80
	#创建Image对象
	image = Image.new('RGB',(width,height),(255,255,255))
	draw = ImageDraw.Draw(image)

	#画图片背景
	for w in range(width):
		for h in range(height):
			#随机生成北景色
			ranBgColor = (random.randint(128,255),random.randint(128,255),random.randint(128,255))
			draw.point((w,h),fill=ranBgColor)
	#生成安全码
	for sec in range(secNum):
		#生成随机字符
		ranChar = chr(random.randint(65,90))
		print('ranchar:',ranChar)
		#随机生成文本颜色
		ranTextColor = (random.randint(20,127),random.randint(20,127),random.randint(20,127)) 
		print('ranTextColor:',ranTextColor)
		draw.text((80*sec+18,26),ranChar,font=font,fill=ranTextColor)
	#模糊化：
	image = image.filter(ImageFilter.BLUR)
	image.save('mySecuriteImage.jpeg','jpeg')

#test_main测试：
if __name__ =='__main__':
	out=genernateSecImage(4)

