import socket
host = socket.gethostbyname(socket.gethostname())
print(host)  # ---> 10.247.6.145

'''

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . :
   IPv6 Address. . . . . . . . . . . : 2405:e640:c001::83e
   Link-local IPv6 Address . . . . . : fe80::8bc8:332:b9d1:e7e7%17
   IPv4 Address. . . . . . . . . . . : 10.247.6.145
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : fe80::7e5a:1cff:fe81:8bcb%17
                                       10.247.6.1
'''

HOST = '10.247.6.145'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
    communication_socket.send(f"Got your message! Thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")

