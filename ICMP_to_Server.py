#/usr/bin/Python

# Basic Python ICMP to a Domain

import os

hostname = "www.google.com"
response = os.system("ping -c 1" + hostname)

if response == 0:
  print hostname, "is up and responding..." # ICMP response will send a non-zero number if it fails 
else:
  print hostname, "is down at this time..."
