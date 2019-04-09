from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


text = u'8'

im = Image.open('001.jpeg')
font_size=int(50*im.size[1]/200)
font = ImageFont.truetype("Arial.ttf", font_size)
dr = ImageDraw.Draw(im)
dr.text((im.size[0]*0.92,0),text,(255,134,230),font=font)

im.show()
im.save('test001.jpeg')