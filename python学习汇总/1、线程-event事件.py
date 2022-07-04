import threading
import time

# event = threading.Event()
#
# event.clear() # 重置代码中的event对象，使得所有该event事件都处于待命状态
#
# event.wait() # 阻塞线程，等待event指令
#
# event.set() # 发送event指令，使的所有设置了该event事件的线程执行

class MyThread(threading.Thread):

    def __init__(self,event):
        super().__init__()
        self.event = event


    def run(self):
        print("线程{}已经准备完毕".format(self.name))
        self.event.wait() # 阻塞线程

        print("{}开始执行...".format(self.name))


if __name__=="__main__":
    event=threading.Event()
    threads = []

    [threads.append(MyThread(event)) for i in range(1,10)]
    print(threads)
    event.clear()
    [t.start() for t in threads] # t.start()表示启动状态，但是会在run()函数中的self.event.wait()中阻塞，停止

    time.sleep(5)
    event.set() #这句之后，才会执行run()函数中 self.event.wait() 下面的代码


