import socketserver
import TESTSQL
import datetime
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        addr = self.client_address
        #参数说明
        #AA0 插入CDK
        #AA1 登录
        #AA2 检查是否到期
        #AA3 查询机器码
        #AA4 删除CDK
        #AA5 检查开始时间
        accept_data = str(conn.recv(1024), encoding="utf8")
        if accept_data.find('AA0|') >= 0:
            temp=accept_data[4:]
            print('时间 = '+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'命令 = ' + accept_data, addr)
            temp_arr = temp.split('|')
            ret_AA0 = QL.增('gld',temp_arr[0],temp_arr[1])
            conn.send(str(ret_AA0).encode())
        elif accept_data.find('AA1|') >= 0:
            temp = accept_data[4:]
            print('时间 = ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '命令 = ' + accept_data, addr)
            temp_arr = temp.split('|')
            ret_AA1 = QL.login('gld', temp_arr[0],temp_arr[1],addr[0])
            conn.send(str(ret_AA1).encode())
        elif accept_data.find('AA2|') >= 0:
            temp = accept_data[4:]
            print('时间 = ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '命令 = ' + accept_data, addr)
            temp_arr = temp.split('|')
            ret_AA2 = QL.查('gld',temp_arr[0],temp_arr[1])
            conn.send(str(ret_AA2).encode())
        elif accept_data.find('AA3|') >= 0:
            temp = accept_data[4:]
            print('时间 = ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '命令 = ' + accept_data, addr)
            ret_AA3 = QL.查询机器码('gld', temp)
            conn.send(str(ret_AA3).encode())
        elif accept_data.find('BB0') >= 0:
            ret_BB0 = QL.检查版本()
            conn.send(str(ret_BB0).encode())
        conn.close()
if __name__ == '__main__':
    print('服务器启动')
    QL = TESTSQL.MYSQL(2206,'root','Zddaa1122','mydb')
    sever = socketserver.ThreadingTCPServer(("172.31.38.183", 8680),MyServer)
    sever.serve_forever()
