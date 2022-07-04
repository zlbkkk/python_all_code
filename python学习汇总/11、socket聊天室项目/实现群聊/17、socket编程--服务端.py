import socket
import threading

# 群聊实现思路：服务端接收到任一客户端的消息，服务端再把它转发给其他的客户端


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",8000)) # 端口必须不可占用
server.listen()

print("服务器已经启动")

# sock,addr = server.accept() # accept() 是阻塞方法，addr是客户端的地址对象

client_sockets = []  #接收客户端的连接对象


def handle_socket(sock):
    while True:
        data = sock.recv(1024)
        # 服务端接收到任一客户端的消息，服务端再把它转发给其他的客户端
        # send_data =

        print(data.decode("utf-8"))
        re_data = input("服务端请输入:")
        sock.send(re_data.encode())


while True:
    sock, addr = server.accept()  # accept() 是阻塞方法，addr是客户端的连接对象
    client_sockets.append(sock)
    client_thread = threading.Thread(target=handle_socket,args=(sock,))
    client_thread.start()


# server.close()
# sock.close()


