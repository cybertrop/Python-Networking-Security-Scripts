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

# I'd like to note that we can view this traffic with tcpdump and then create content around it for monitoring purposes
# For example we can monitor socket connections to sensitive zones/servers (I dont often see socket monitoring implemented)

# So anyways... 
# Once you run this Python program you can open up tcpdump and run the following command BEFORE running the Python CMD

# $ sudo tcpdump -i en0 -nn -s0 -v port 80 >> input.txt ; cat input.txt | grep "HTTP" 

# Once you run the TCPDump script it will prompt you for login/passwd ... from there after the python execution completes...
# you can CTRL + C out of the tcpdump script and then you will automatically see the connection occuring via PCAP
