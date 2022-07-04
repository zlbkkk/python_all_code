import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("127.0.0.1",8080))

while True:
    # msg = input(">>>:")
    client.send(b"hello word")
    data = client.recv(1024)
    print(data)


