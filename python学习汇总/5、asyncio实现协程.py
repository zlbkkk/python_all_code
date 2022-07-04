import asyncio

async def hello(name):
    print("hello",name)

coro = hello("world") #1、创建协程对象

loop = asyncio.get_event_loop() # 2、获取事件循环对象容器

task = loop.create_task(coro) # 3、将协程对象转化为task
# task = asyncio.ensure_future(coro) 这个和上面那个一样的效果

loop.run_until_complete(task)# 4、将task任务扔进事件循环对象中触发