#!/usr/bin/python

# This is a script creating a UDP Client on the fly; remember connectionless ...

# Importing the appropriate module
import socket

# Setting the proper host and port
target_host = "www.google.com"
target_port = 80

# Creating a socket object but using the SOCK_DGRAM for UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# No need to connect in this script because UDP is connectionless
client.sendto("Hostname", (target_host, target_port))

# Receiving data and details from our host
data, addr = client.recvfrom(4096)

print data
