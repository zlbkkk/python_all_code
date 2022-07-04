from gevent import monkey;monkey.patch_all()
from gevent import spawn
import time



def heng():
    print("哼")
    time.sleep(2)
    print("哼")


def ha():
    print("哼")
    time.sleep(2)
    print("哼")


start_time = time.time()
g1=spawn(heng)
g2=spawn(ha)

# 以下的.join()必须要加入，要不然函数没运行完就退出了，是固定写法
g1.join()
g2.join()

print(time.time())