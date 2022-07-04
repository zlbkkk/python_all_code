#第一种方法：使用sorted函数 --- 思路一：排序



#第二种方法：使用heapq--- 思路二：堆排序
# heapq.nlargest(a, 2),如，返回[45,8] 返回的列表会按照从小到大排列好
import heapq

def findKthLargest(k,nums):  # 注意nums是列表，k是一个数
    print(heapq.nlargest(k, nums))
    return heapq.nlargest(k, nums)[-1]

a=[1,3,2,8,3,45,3,0]

print(findKthLargest(a,3))


# 第三种方法

