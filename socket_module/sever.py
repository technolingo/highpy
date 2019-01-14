import socket


host = 'localhost'
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(1)
print(f'Listening for requests on port {port}...')

conn, addr = s.accept()
print(f'Connection established for {addr}')

conn.send('Hello World!'.encode())

conn.close()
print('Connection terminated.')
