import socket

SERVER_IP = '10.12.50.241'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(SERVER_IP, SERVER_PORT)
    print(s.recv(1024))

input()