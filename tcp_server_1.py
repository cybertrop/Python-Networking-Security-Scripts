#!/bin/python

# TCP Server

import socket
import os
# Sockstream is TCP .. DGRAM is UDP 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is used to specify the protocol used for comomunication socket family = IPv4 

host = socket.gethostname()
port = 444

# Now we need to bind the values (port and host)

server_socket.bind(('172.16.219.1', port)) # Make the host an IP here as a string 

# Now setup a TCP Listener to listen to the client - 3 connections 

server_socket.listen(3)

while True:
	client_socket, address = server_socket.accept() # Accepts TCP Connection from client

	print("*** Received connection from %s" % str(address)) #%s converts to string .. %r wrapper to make the statement unambiguous 
		# not printed out in the tradional way of a string

	message = '*** Welcome to the TCP Server *** ' + '\r\n' # \r go to the next line 


	client_socket.send(message.encode('ascii')) # Specify the encoding type ..

	client_socket.close()
