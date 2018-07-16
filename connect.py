#!/usr/bin/env python
from socket import *
def sends(cmds,can):
    HOST = '47.105.51.67'
    PORT = 8680
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    try:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        tcpCliSock.send((cmds + '|' + can).encode())
        ret = str(tcpCliSock.recv(BUFSIZ), encoding="utf8")
        tcpCliSock.close()
        return ret
    except:
        print('发送日志失败')
        return ''
def addcdk(can):
    return sends('AA0', can)
def login(can):
    return sends('AA1', can)
def get(can):
    return sends('AA2', can)
def getcode(can):
    return sends('AA3', can)
def getver(can):
    return sends('BB0', can)
def LAN_jietu():
    with open('temp.jpg', 'r') as file_object:
        contents = file_object.read()
    return sends('A1', str(contents))
if __name__ == '__main__':
    getcode('SXFZ9HJOQ5W4A7HM0JU07YQK78YL9N1ZYH8')