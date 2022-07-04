

class Queue:

    def __init__(self):
        self.__list = []


    def add_front(self,item):
        # 在头部添加item
        self.__list.insert(0,item)

    def add_end(self,item):
        # 在尾部添加item
        self.__list.insert(0,item)



    def pop_front(self):
    # 从队列头部取一个元素

        self.__list.pop(0)

    def pop_end(self):
    # 从队列尾部取/删除一个元素
        self.__list.pop()


    def is_empty(self):
    # 判断一个队列是否为空
        return self.__list == []

    def size(self):
    # 返回队列的大小
        return len(self.__list)