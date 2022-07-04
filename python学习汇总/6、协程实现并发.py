import asyncio
import time

#定义协程
async def do_some_work(x):
    print("等待：",x)
    await asyncio.sleep(x)
    return "等待时间:{}".format(x)


if __name__ == '__main__':

    start_time = time.time()
    #创建多个协程对象
    coro1 = do_some_work(1)
    coro2 = do_some_work(2)
    coro3 = do_some_work(3)

    #将协程对象转换为task，并组成一个list
    tasks =[
        asyncio.ensure_future(coro1),
        asyncio.ensure_future(coro2),
        asyncio.ensure_future(coro3)
    ]

    #将task注册到事件循环中
    # 两种方法： asyncio.wait和asyncio.gather
    loop = asyncio.get_event_loop()

    # loop.run_until_complete(asyncio.wait(tasks)) # wait方法只接受列表作为参数
    loop.run_until_complete(asyncio.gather(*tasks)) #gather方法接收不定量参数，和上面的asyncio.wait(tasks)一样的效果
    for task in tasks:
        print("任务返回的结果是：",task.result())

    print("运行的总时间是：",time.time()-start_time)