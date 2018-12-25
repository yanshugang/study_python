import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        return_data = input()
        sock.send(return_data.encode('utf-8'))


# 获取从客户端发送的数据, 一次获取1k的数据。
while True:
    sock, addr = server.accept()

    # 使用线程处理多个连接
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
