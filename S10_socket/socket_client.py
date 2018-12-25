import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))

while True:
    send_data = input("client-请输入：")
    client.send(send_data.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))
