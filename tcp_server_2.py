#!/bin/python

# TCP Server Version 2

import socket

HOST = '127.0.0.1'
port = 444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT)) # Bind is used to associate the socket with a specific network interface or port number 
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by' addr)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(data)


