#网络编程实例练习
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('mysocket:',s)

hostname="www.sina.com.cn"
port = 80
s.connect((hostname,port))
#发送请求
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接受数据
buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)
s.close()


header,html= data.split(b'\r\n\r\n',1)

print(header.decode('utf-8'))

with open('saves.html','wb') as myfile:
	myfile.write(html)
	myfile.close()






