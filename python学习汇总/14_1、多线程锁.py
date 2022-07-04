
from threading import Thread, Lock
import time

money = 16

l = Lock()

def task():
    global money
    l.acquire()
    tem = money
    time.sleep(0.1)
    money = tem -1
    l.release()

    # 加锁也可以用with这样的写法，但是推荐用上面l.acquire()的写法
    # with l:
    #     tem = money
    #     time.sleep(0.1)
    #     money = tem -1


if __name__ == '__main__':
    t_list=[]

    for i in range(10):
        t = Thread(target=task)
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    print(money)
