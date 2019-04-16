#client test
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host,port))
reciveInfos = []
while True:
	d = s.recv(1024)
	if d:
		reciveInfos.append(d)
	else:
		break
s.close()
print('Infomationg:',b''.join(reciveInfos))