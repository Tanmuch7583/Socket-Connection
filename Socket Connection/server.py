import socket


SERVER_IP = '10.12.50.241'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print("Server listening for a connection......")
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection established from: {addr}')

    with conn:
        while True:
            s.send(b"Hello There")
            break
