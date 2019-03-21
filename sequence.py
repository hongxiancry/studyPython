#关于列表和元组的学习
#列表

edward = ['Edward Gumby',4]
john = ['John Smith',5]
database = [edward,john]
print(database)
greeting = 'Hello'
print(greeting[0])
print(greeting[-1])
print(greeting[-2])
year = input("year : ")[3]
print(year)
print(len(year))
months = ['January','February','March','April','May','June','July','August','September','October','Novemeber','December']
endings = ['st','nd','rd']+17*['th']\
          +['st','nd','rd'] + 7 * ['th']\
          +['st']
year = input('please input year: ')
month = input('please input month(1-12): ')
day = input('please input day(1-31): ')
month_number = int(month)
day_number = int(day)
month_name = months[month_number-1]
ordinal = day + endings[day_number-1]
print(month_name+' '+ordinal+' '+year)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[4:9])
print(numbers[-4:-1])
print(numbers[1:])
print(numbers[-3:])
print(numbers[:5])
print(numbers[:-3])

url = 'http://www.python.org'
print('domain:',url[11:-4])
print(numbers[0:10:2])
print(numbers[1:10:2])
print(numbers[::4])
print(numbers[::-2])
print(numbers[5::-2])
number = numbers[0:10:2]+numbers[1:10:4]
print(number[0:])
number = numbers[0:10:2]*2
print(number)

sentence = input('sentence: ')
uptext_width = len(sentence)*2
downtext_width = len(sentence)*2
leftmargin = ' '*3
print('-'*uptext_width)
print(leftmargin+sentence)
print('-'*downtext_width)

right = 'rw'
print('r' in right)
print('m' in right)
print(not 'm' in right)
user_name = ['lili','shahs','may']
inputname = input('input your name: ')
print(inputname in user_name)

database = [['lisa',123],['jj',56],['ll',89]]
name = input('please input your name: ')
pn = int(input('please input your pn: '))
print([name,pn] in database)
if [name,pn] in database :
	print("access granted!")
else :
	print("access denied!")
	
numbers = [123,20,345]
print(len(numbers))
print(max(numbers))
print(min(numbers))

