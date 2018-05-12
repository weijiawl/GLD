import socketserver  # 导入socketserver模块
import os
class MyServer(socketserver.BaseRequestHandler):  # 创建一个类，继承自socketserver模块下的BaseRequestHandler类
    def handle(self):  # 要想实现并发效果必须重写父类中的handler方法，在此方法中实现服务端的逻辑代码（不用再写连接准备，包括bind()、listen()、accept()方法）
        conn = self.request
        addr = self.client_address
        # 上面两行代码，等于 conn,addr = socket.accept()，只不过在socketserver模块中已经替我们包装好了，还替我们包装了包括bind()、listen()、accept()方法
        while 1:
                accept_data = str(conn.recv(1024), encoding="utf8")
                if accept_data.find('bb') >= 0:
                    print(str(addr) + '<检查版本>')
                    with open('c:/FtpData/ver/ver.txt', 'r') as f:
                        conn.sendall(f.read().encode())
                    break
                elif accept_data.find('jl') >= 0:
                    print(str(addr) + '<记录信息>')
                    #格式=jl|用户|类型|账号|文本|时间
                    accept_data_arr = accept_data.split('|')
                    with open('c:/FtpData/Data/' + accept_data_arr[1] + '/'+ accept_data_arr[2] +'.txt', 'a+') as f:
                        f.write(accept_data + '\n')
                    break
                elif accept_data.find('cj') >= 0:
                    print(str(addr) + '<创建用户>')
                    #格式=cj|目录
                    accept_data_arr = accept_data.split('|')
                    if not os.path.isdir(accept_data_arr[1]):
                        os.makedirs(accept_data_arr[1])
                    break
        conn.close()
if __name__ == '__main__':
    sever = socketserver.ThreadingTCPServer(("172.26.232.52", 8680),MyServer)  # 传入 端口地址 和 我们新建的继承自socketserver模块下的BaseRequestHandler类  实例化对象
    sever.serve_forever()  # 通过调用对象的serve_forever()方法来激活服务端
