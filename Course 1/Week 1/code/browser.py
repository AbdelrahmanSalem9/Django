import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9000))               # This IP address allows the machine to connect to and communicate with itself
cmd = 'GET http://127.0.0.1/page1_htm HTTP/1.0\r\n\r\n'.encode() # python use unicode so we need to convert it to UTF-8
print(f"Encoded Version of CMD {cmd}")
s.send(cmd)

while True:
    data = s.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

s.close()

"""
This code works the same but this operate on the HTTP level where socket is low level network opeartion
Note The Response MUST be in a correct format
"""
# import urllib.request
# fhand = urllib.request.urlopen("http://127.0.0.1:9000/test.txt")
# for line in fhand:
#     print(line.decode())
