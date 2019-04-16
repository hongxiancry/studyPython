import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

hostname = socket.gethostname()
s.bind((hostname,1234))

s.listen(5)
while True:
	c,addr = s.accept()
	print('addr:',addr)
	c.send(b'Thank you for your visiting!')
	c.close()
