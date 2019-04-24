#--*--utf-8 coding --*--
'第 0009 题：一个HTML文件，找出里面的链接。'
__author__='chairuiya'

from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.links = []
	def handle_starttag(self, tag, attrs):
		if tag=='a':
			for (varaibles,value) in attrs:
				if varaibles == 'href':
					self.links.append(value)
				else:
					pass
		else:
			pass


#test_main
if __name__ == '__main__':
	htmltext = '<html><div>htmltest</div><a href="www.google.com"> google.com</a> <A Href="www.pythonclub.org"> PythonClub </a> <A HREF = "www.sina.com.cn"> Sina </a> </html>'
	mytest = myHTMLParser()
	mytest.feed(htmltext)
	print("links:",mytest.links)


