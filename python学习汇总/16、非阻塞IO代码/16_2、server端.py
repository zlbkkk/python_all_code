import socket


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",8080))
server.listen(5)

server.setblocking(False) #将所有的网络阻塞变成非阻塞 ，accept() recv()
r_list = []
del_list = [] # 存放要删除的连接
while True:
    try:
        conn,addr = server.accept()
        r_list.append(conn)

    except BlockingIOError as e: # 如果上面没有客户端来accept()，就会一直执行except这里的代码
        # print("做其他事")

        for conn in r_list:
            try:
                data = conn.recv(1024)
                if len(data)==0:
                    conn.close() #关闭conn
                    del_list.append(conn) #将无用的连接放到这个列表中，为后面删除做准备
                    continue

                print(data)
                conn.send(data.upper()) #给客户端发送消息

            except BlockingIOError:
                continue  # 这个continue是对上面的r_list中的连接进行处理，假设for循环遍历出来第一个conn没有数据，走了except，则不进行下面的操作，继续返回回去遍历

            except ConnectionResetError: # 如果客户端关闭了连接，服务端也要关闭连接
                conn.close()
                del_list.append(conn)

        for conn in del_list: # 循环遍历删除无用连接
            r_list.remove(conn)

        del_list.clear()