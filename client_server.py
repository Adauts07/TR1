import socket


def TCPclient(host, port):
    tcp_client = socket.socket(socket.AF_INET, socket.SOCKS_STREAM)
    tcp_client.connect((host, port))
    status = tcp_client.send(b'message')
    if status > 0:
        data = tcp_client.recv(1024)

    tcp_client.close()


def TCPserver(host, port):
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((host, port))
    tcp_server.listen()
    conn, addr = tcp_server.accept()

    while 1:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode('utf8'))

        conn.sendall(data)
    conn.close()
