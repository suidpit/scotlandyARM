import socket
import sys


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	print('Connecting...')
	s.connect(("192.168.1.10", 12007))
	s.send("PROVA".encode())


