#!/usr/bin/env python

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("", 54899))

import sys
s.send(sys.argv[1]+ '  ' + sys.argv[2] + "\n")

print s.recv(1024)
s.close()
