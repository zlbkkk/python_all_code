import socket

def send_file_to_client(new_client_socket,client_addr):

    file_name = new_client_socket.recv(1024).decode("utf-8") #接收客户端传过来的数据，也就是file_name
    print("客户端(%s)需要下载的文件是：%s" % (str(client_addr), file_name))

    file_contend = None # 标记是否开了了文件
    #打开文件，读取数据，发送文件中的数据给客户端
    try:
        f = open("c:\\2.txt","rb")
        file_contend = f.read()  # 这个在下面的if file_contend中会判断
        f.close()
    except Exception as e:
        print("没有下载的文件(%s)"%file_name)


    if file_contend:
        # new_client_socket.send(file_contend.decode())  不需要decode()
        new_client_socket.send(file_contend) # file_contend在上面是rb读出来的，本来就是二进制，不需要 file_contend.decode()

def main():

    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_server_socket.bind(("0.0.0.0",7890))
    tcp_server_socket.listen()

    while True:
        new_client_socket,client_addr = tcp_server_socket.accept()

        # 接收客户端发过来的要下载的文件名
        # file_name = new_client_socket.recv(1024).decode("utf-8")

        # print("客户端(%s)需要下载的文件是：%s"% (str(client_addr),file_name))

        # new_client_socket.send("hahahhahazlb---ok".encode("utf-8"))

        #这里替换成调用那个函数
        send_file_to_client(new_client_socket,client_addr) # 调用发送数据的函数

        new_client_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    main()

