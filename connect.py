#!/usr/bin/env python
from socket import *
import time
HOST = 'localhost'
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
tcpCliSock.send('bb'.encode())
data = tcpCliSock.recv(BUFSIZ)
if data:
    print(data.decode('utf-8'))
    tcpCliSock.send('bye'.encode())
    time.sleep(5)

#tcpCliSock.close()