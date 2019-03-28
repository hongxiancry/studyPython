
'''
try:
	x = int(input('Enter first number:'))
	y = int(input('Enter second number:'))
	print(x/y)
except ZeroDivisionError:
	print('check the seconde number can not be zero!')
except TypeError:
	print('check the number can not be str!')
except ValueError:
	print('check the number should be str')
try:
	x = int(input('Enter first number:'))
	y = int(input('Enter second number:'))
	print(x/y)
except:
	print('check the number should be a number')
	
while True:
	try:
		x = int(input('Enter first number:'))
		y = int(input('Enter second number:'))
		print(x/y)
	except:
		print('check the number should be a number')
	else:
		break
		'''
try:
	x = 5
	y = int(input('Enter second number:'))
	print(x/y)
except:
	print('check the second number!')
finally:
	print('finally print the words!')
def faulty():
	raise Exception('someting is wrong!')
def ignore_faulty():
	faulty()
def handle_exception():
	try:
		faulty()
	except:
		print('exception handle')
ignore_faulty()