from __future__ import print_function
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('localhost',30000))
print("socket binded")
s.listen(30)
print("socket listening")
while True:
	conn, abc=s.accept()
	print("connected with ",abc[0],"with: " ,abc[1])
	xyz=conn.recv(1024)
	print(str(xyz))
	print('jeb mein rakha cash hai!!')

#s.send(m2)