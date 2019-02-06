#!/bin/python

# TCP CLIENT

import socket
import os

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 # target host is the ip address of target server 
target_host = socket.gethostname()
target_port = 444

client_socket.connect((target_host, target_port)) # Enter iP here 

message = client_socket.recv(1024)

client_socket.close()

print(message.decode('ascii'))


