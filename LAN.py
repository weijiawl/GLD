from socket import *
import time
from PIL import ImageGrab
class LAN_CLASS:
    tcpCliSock = ""
    def 截图(x,y,x1,y1,name):
        bbox = (x,y,x1,y1)
        im = ImageGrab.grab(bbox)
        im.save(name)
    def loop():
        while True:
            try:
                HOST = '192.168.0.88'
                PORT = 8989
                BUFSIZ = 1024
                ADDR = (HOST, PORT)
                tcpCliSock = socket(AF_INET, SOCK_STREAM)
                tcpCliSock.connect(ADDR)
                tcpCliSock.settimeout(60)
                while True:
                    try:
                        accept_data = tcpCliSock.recv(1024).decode()
                        if accept_data == 'jietu':
                            截图(0,0,800,600,os.getcwd() + "/temp.jpg")
                            with open('./temp.jpg', 'rb') as f:
                                for data in f:
                                    tcpCliSock.send('JT'.encode() + data)
                                    accept_data = tcpCliSock.recv(1024).decode()
                            tcpCliSock.send('JS'.encode())
                        tcpCliSock.send('RJ'.encode())#检查主机状态顺带发送心跳
                    except:
                        tcpCliSock.send('RJ'.encode())#检查主机状态顺带发送心跳
            except:
                time.sleep(2)
            #ret = str(tcpCliSock.recv(BUFSIZ), encoding="utf8")
            #tcpCliSock.close()
    def LAN_F(str):
        try:
            tcpCliSock.send('JS'.encode())
        except:
            HOST = '192.168.0.88'
            PORT = 8989
            BUFSIZ = 1024
            ADDR = (HOST, PORT)
            tcpCliSock = socket(AF_INET, SOCK_STREAM)
            tcpCliSock.connect(ADDR)
            tcpCliSock.settimeout(60)