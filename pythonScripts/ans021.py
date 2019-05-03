#--utf-8*--
'通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。'
__author__='chairuiya'

'''
step1 加密算法
step2 验证密码是否正确
'''
import os,sys
from hashlib import sha256
import hmac

#加密
def encrypt_pass(password,salt=None):
	#生成随机盐
	if salt==None:
		salt = os.urandom(8)
	assert isinstance(password,str)
	password = password.encode('utf-8')
	assert isinstance(password,bytes)
	#经过10次叠加加密
	for i in range(10):
		hashed = hmac.digest(password,salt,sha256)
	encrypt_result = salt+hashed
	return encrypt_result

#验证密码是否正确
def validate_password(input_pass,hashed):
	return hashed == encrypt_pass(input_pass,hashed[:8])

#test_main
if __name__ == '__main__':
	hashed = encrypt_pass('login')
	#print(hashed)
	input_pass = input('please input your password:')
	loginResult = validate_password(input_pass,hashed)
	if loginResult:
		print('login status:success login!')
	else:
		print('login status:password is wrong!')

