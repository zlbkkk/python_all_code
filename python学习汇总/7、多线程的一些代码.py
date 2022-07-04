import threading
from concurrent.futures import ThreadPoolExecutor

# 1、使用回调函数去获取结果

# def action(n):
#     my_sum=0
#     for i in range(n):
#         print(threading.current_thread().name + " " + str(i))
#         my_sum += 1
#     return my_sum
#
# def get_result(f):
#     print(f.result())
#
# with ThreadPoolExecutor(max_workers=3) as pool:
#     f1 = pool.submit(action, 2)
#     f2 = pool.submit(action, 2)
#
#     f1.add_done_callback(get_result)
#     f2.add_done_callback(get_result)

# 案例2：使用map方法来启动多线程以及收集执行结果
#
# from concurrent.futures import ThreadPoolExecutor
# import threading
# import time
#
# # 定义一个准备作为线程任务的函数
# def action(max):
#     my_sum = 0
#     for i in range(max):
#         print(threading.current_thread().name + '  ' + str(i))
#         my_sum += i
#     return my_sum
#
# # 创建一个包含4条线程的线程池
# with ThreadPoolExecutor(max_workers=4) as pool:
#
#     # 使用线程执行map计算
#     results = pool.map(action, (2, 3, 4,5,6,7,8,9,10))  # 后面元组有3个元素，因此程序启动3条线程来执行action函数
#     print('--------------')
#     for r in results:
#         print(r)


from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print(f"{threading.current_thread().name} get page {times}s finished")
    return times

executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4] # 并不是真的url
# all_task = [executor.submit(get_html, (url)) for url in urls]
result = executor.map(get_html,(2,3,4))
for i in result:
    print(f"执行的结果为{i}")



# for future in as_completed(all_task):
#     data = future.result()
#     print("in main: get page {}s success".format(data))
