import random
from threading import Thread, Lock
import time

money = 16

l = Lock()

def task():
    global money
    tem = money
    # time.sleep(0.1)
    money = tem -1
#
# 执行结果说明：
#     1、如果time.sleep(0.1)被注释掉，name每一个线程都会去抢这个GIL，同一时间只会有一个线程抢到，然后执行tem-1的操作，
#         然后释放，另外一个线程在执行-1，所以最后结果是6，是正确的的；

#     2、但是如果 time.sleep(0.1)存在，当一个线程执行到time.sleep(0.1)时，会挂起，实际情况是：遇到IO，会挂起，
#           那么另外的线程就会抢到GIL，此时每个线程都是16-1，所以最后结果是 15



if __name__ == '__main__':
    t_list=[]

    for i in range(10):
        t = Thread(target=task)
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    print(money)




