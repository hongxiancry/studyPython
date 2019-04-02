#/Users/chairuiya/Documents/learn/studyPython
#_*_ utf-8 _*_
'module script1'
__author__ = 'chairuiya'

def _private_1(name):
	return 'Hello %s' %name
def _private_2(name):
	return 'hi %s' % name

def greeting(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)
if __name__== '__main__':
	print(greeting('lisa'))
