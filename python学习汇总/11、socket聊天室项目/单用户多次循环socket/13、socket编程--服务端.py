import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",8000)) # 端口必须不可占用
server.listen()

print("服务器已经启动")

sock,addr = server.accept() # accept() 是阻塞方法，addr是客户端的地址对象

while True:
    print('Accept new connection from %s:%s...' % addr)
    data = sock.recv(1024) # 指定一次性接收1k的数据
    print(data.decode("utf-8")) # 通过sock对象接收的是bytes类型的数据，需要解码之后才能正确显示为str

    # 如果收到的是886则断开
    if data.decode()=="886":
        break

    re_data = input()
    sock.send(re_data.encode())

server.close()
sock.close()





