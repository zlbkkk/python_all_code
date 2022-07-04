from concurrent.futures import ThreadPoolExecutor
import time

pool = ThreadPoolExecutor(max_workers=5)

def task(n):
    print("线程%s"%n)
    time.sleep(2)
    return ("线程%d相乘的结果是%d"%(n,n**n))

t_list = []

for i in range(10):
    res = pool.submit(task,i) # 提交20个任务到线程池
    t_list.append(res) # 先将每个线程的结果保存到列表中

# pool.shutdown() 等待线城池中所有任务都执行完之后在执行下面的代码,如果没有这个，那线程运行和获取结果就会夹杂着
pool.shutdown() # 关闭线程池 等待线城池中所有任务运行完毕

for t in t_list:
    print(">>>:",t.result())  # 获取每一个线程执行的结果，是有序的 线程1 线程2 线程3的结果 .....、


