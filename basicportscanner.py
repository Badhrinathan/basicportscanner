#!/usr/bin/python  


import pyfiglet
import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

banner = pyfiglet.figlet_format("P o r t s c a n n e r", font = "slant"  )
print(banner)
print("." * 70 + "by badboy")
host = raw_input("[*] Enter Host to scan: ")

def scanner(port):
          if sock.connect_ex((host, port)):
              print("[-]Port %d is closed" % (port))
          else:
              print("[+]port %d is open" % (port))

for port in range(1,1000):
       scanner(port)
print(datetime.now())
