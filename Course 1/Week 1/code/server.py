from http import client, server
import socket 
my_local_IP = socket.gethostbyname(socket.gethostname())

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost',9000))
server_socket.listen(5)             # request the OS to queue up to 5 request when the server is busy

print("Server is Listining on port 9000")
while True:
    (client_socket,client_adrs) = server_socket.accept()

    recv_data = client_socket.recv(5000).decode()
    pieces = recv_data.split("\n")
    if(len(pieces) > 0):
        print(pieces[0])
    
    data = "HTTP/1.1 200 OK\r\n"
    data += "Content-Type: text/html; charset=utf-8\r\n"
    data += "\r\n"
    data += "<html><body>Hello World</body></html>\r\n\r\n"

    # Response can be in any format but the client application need to understand it
    # data = "SERVER DATA !"
    client_socket.sendall(data.encode())
    client_socket.shutdown(socket.SHUT_WR)

server_socket.close()

