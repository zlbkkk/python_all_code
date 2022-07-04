import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",7890))
server.listen()

def talk(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:break
            print(data.decode("utf-8"))
            conn.send(data.upper())
        except ConnectionResetError as e:
            print(e)
            break


    conn.close()

while True:
    conn,addr = server.accept()
    t = threading.Thread(target=talk,args=(conn,))

    t.start()



