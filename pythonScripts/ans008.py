#-*- coding: utf-8 -*-
'第 0008 题：一个HTML文件，找出里面的正文。'

__author__='chairuiya'

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
	is_body = False

	def handle_starttag(self, tag, attrs):
		if tag == "body" :
			self.is_body = True
			print("Encountered a start tag:", tag)
		else:
			pass
	def handle_endtag(self, tag):
		if tag == "body" :
			self.iis_body = False
			print("Encountered an end tag :", tag)
		else:
			pass

	def handle_data(self, data):
		if self.is_body :
			print("Encountered some data:", data)
		else:
			pass

#test_main
if __name__ =='__main__':
	parser = MyHTMLParser()
	parser.feed('<html><head><title>Test</title></head>'
		'<body><h1>Parse me!aibndieng</h1><h2>testmyhtml</h2></body></html>')
	parser.close()