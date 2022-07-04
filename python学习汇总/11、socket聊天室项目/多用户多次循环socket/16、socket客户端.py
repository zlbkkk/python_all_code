import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("127.0.0.1",8000))


while True:
    try:
        to_data = input("客户端请输入:")
        client.send(to_data.encode())
        data = client.recv(1024)
        print(data.decode())
        #如果收到的是886则断开
        if data.decode()=="886":
            break

    except ConnectionAbortedError:
        break


client.close()


