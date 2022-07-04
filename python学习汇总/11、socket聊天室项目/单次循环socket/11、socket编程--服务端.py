import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",8000)) # 端口必须不可占用

server.listen()
sock,addr = server.accept() # accept() 是阻塞方法，addr是客户端的地址对象

data = sock.recv(1024) # 指定一次性接收1k的数据
print(data.decode("utf-8")) # 通过sock对象接收的是bytes类型的数据，需要解码之后才能正确显示为str

sock.send("hello,{}".format(data.decode()).encode())

sock.close()


