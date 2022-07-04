

class Queue:

    def __init__(self):
        self.__list = []


    def enqueue(self,item):
    # 往队列中添加一个item元素
        self.__list.append(item)  #第一种方式
        # self.__list.insert(0,item)  第二种方式

    def dequeue(self):
    # 从队列头部删除一个元素
        self.__list.pop() # 第一种方式
        # self.__list.pop(0) 第二种方式

    def is_empty(self):
    # 判断一个队列是否为空
        return self.__list == []

    def size(self):
    # 返回队列的大小
        return len(self.__list)