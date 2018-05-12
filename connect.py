#!/usr/bin/env python
from socket import *
import datetime
def log(leixing,zhanghao,strs):
    # 格式=jl|类型|账号|文本|时间
    HOST = '47.92.87.126'
    PORT = 8680
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    try:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        date = datetime.datetime.now()
        tcpCliSock.send(('jl|' + leixing + '|' + zhanghao + '|' + strs + '|' + date.strftime('%Y-%m-%d %H:%M:%S')).encode())
    except:
        print('发送日志失败')
log('制裁','542026171','制裁')