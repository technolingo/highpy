import socket


s = socket.socket()
host = 'localhost'
port = 8080

s.connect((host, port))
msg = s.recv(1024)

while msg:
    print(msg.decode())
    msg = s.recv(1024)

s.close()
