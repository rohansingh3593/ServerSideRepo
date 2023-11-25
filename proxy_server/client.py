import socket
host = socket.gethostbyname(socket.gethostname())
print(host)  # ---> 10.247.6.145

HOST = '10.247.6.145'
PORT = 9090

socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("Hello World!".encode('utf-8'))
print(socket.recv(1024))
