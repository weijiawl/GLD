import socket

HOST, PORT = '127.0.0.1', 80
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listen_socket.bind((HOST, PORT))
listen_socket.listen(10)
print('Serving HTTP on port %s ...' % PORT)
GET = "GetIndex"
SET = "SetIndex"
All = False
num = 0
Index = 0
with open("D:/Index.txt","r",encoding="utf-8") as f:
     T=int(f.read())
     print(T)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024).decode()
    print(request)
    #returns.encode('utf-8')
    if request.find(SET) > 0:
        if Index >= T:
            All = True
            client_connection.sendall("NO".encode())
        else:
            Index =+ 1
            client_connection.sendall("OK".encode())
        print(str(Index))
    else:
        if request.find(GET) > 0:
            client_connection.sendall(Index.encode())
            if All:
                num =+ 1
                if num >= T-1:
                    Index = 0
                    All = False
                    with open("D:/Index.txt", "r", encoding="utf-8") as f:
                        T = int(f.read())



    client_connection.close()