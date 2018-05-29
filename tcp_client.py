#!/usr/bin/python

# Simple TCP Client Script

# Import appropriate module
import socket

# Set our targets
target_host = "www.google.com"
target_port = 80

# Creating a socket object and setting it to our variable client
# AF_INET is the socket module domain type for IPv4 addressing;  while SOCK_STREAM is used for TCP connections
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to our client via the connect function
client.connect((target_host, target_port))

# Seding out HTTP data to the host
client.send("GET / HTTP/1.1\r\n Host: google.com\r\n\r\n")

# Receiving an appropriate response
response = client.recv(4096)

print response
