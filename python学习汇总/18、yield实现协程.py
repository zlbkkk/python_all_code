
# 实现携程的方式1
def consumer():
    r=""
    while True:
        n = yield r
        if not n:
            return
        print(f"【consumer】consuming {n}")
        r='200 ok'


def product(c):
    c.send(None)
    n=1
    while n<5:

        print(f"【product】 producting {n}")
        r = c.send(n)

        print(f"[product] consumer return {r}")
        n += 1

c=consumer()

product(c)

# 实现携程的方式2===========================
from gevent import monkey;monkey.patch_all()
import time
from gevent import spawn

def heng():
    print("哼")
    time.sleep(2)
    print("heng")

def ha():
    print("哈")
    time.sleep(2)
    print("ha")

start = time.time()
g1=spawn(heng)
g2 = spawn(ha)

g1.join()
g2.join()
print(time.time()-start)


print("=============分割线===============")

# 实现协程的方式3========================

import asyncio
start_time=time.time()
async def fun1():
    print(1)
    await asyncio.sleep(2)
    print(2)

async def fun2():
    print(3)
    await asyncio.sleep(2)
    print(4)

async def do_some_work(x):
    print(f"等待：{x}")
    await asyncio.sleep(2)
    return f"等待时间{x}"

coro1 = do_some_work(1)
coro2 = do_some_work(2)
coro3 = do_some_work(3)

# tasks = [
#     asyncio.ensure_future((fun2())),
#     asyncio.ensure_future(fun1())
#
# ]

tasks =[
    asyncio.ensure_future(coro1),
    asyncio.ensure_future(coro2),
    asyncio.ensure_future(coro3)
]

look = asyncio.get_event_loop()
look.run_until_complete(asyncio.gather(*tasks))

for task in tasks:
    # print("任务返回的结果是：",task.print_stack())
    print("任务返回的结果是：",task.result())


print(time.time()-start_time)




# import threading
# import time
# def write_file(path,x):
#     print("正在生成{}个文件".format(x))
#     with open(path,"w") as f:
#         f.write("this is file {}".format(x))
#
# if __name__ == '__main__':
#     import time
#     start_time = time.time()
#     threads = []
#     for i in range(1,1000):
#         t = threading.Thread(target=write_file,args=("d:\\demo\\"+str(i)+".txt",i))
#         t.start()
#
#     # [t.join() for i in threads] # 阻塞主线程
#     print("任务消耗时间为{}".format(time.time()-start_time))


print(time.strftime('%Y-%m-%d %X')) #结果 2020-09-22 17:05:10
print(time.strftime("%Y-%m-%d %X"))