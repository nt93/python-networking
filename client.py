from __future__ import print_function
import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(('localhost',30000))

m1='Apni poori aish hai!'
while True:
	sent = c.send(m1)
