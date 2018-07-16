from socket import *
import time
import threading
import public
import datetime
import configparser

import datetime
starttime = datetime.datetime.now()
#long runnin
endtime = datetime.datetime.now()
d3 = endtime - starttime
print (d3.seconds)


input()

HOST = '127.0.0.1'
PORT = 8989
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
tcpCliSock.settimeout(10)




def get_ini(name, section, option,moren):
    try:
        cf = configparser.ConfigParser()
        cf.read(name)
        temp = cf.get(section, option)
        return temp
    except:
        return moren
numstr = ''

for t in range(500):
    num = get_ini('号.ini', "075N3P22HJOKC0W", str(t + 1), "")
    if num != '':
        numstr = numstr + str(t + 1) + '=' + num + '\n'
    else:
        break
tcpCliSock.send(('ZH' + numstr).encode('gb2312'))



'''
with open('config/记录.ini', 'r') as f:
    data =f.read()
    tcpCliSock.send(('JL' +data).encode('gb2312'))
'''


