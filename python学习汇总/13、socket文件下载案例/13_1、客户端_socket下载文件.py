import socket

tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcp_socket.connect(("127.0.0.1",7890))

download_file = input("请输入要下载的文件名：")
tcp_socket.send(download_file.encode("utf-8"))
recv_data = tcp_socket.recv(1024)

if recv_data: # 判断服务端是否发送过来数据，没发过来就不写入
    with open("c:\\1.txt","wb") as f:
        f.write(recv_data)
else:
    print("服务端没有发送数据")
tcp_socket.close()




