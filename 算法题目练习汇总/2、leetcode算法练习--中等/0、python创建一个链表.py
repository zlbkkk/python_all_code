# 下文参考： https://blog.csdn.net/weixin_42193813/article/details/104246847


# 先创建一个节点类，后续添加节点时，通过这个节点类来创建、添加
# 一个节点由数据和指针组成，下面就是这个意思

class Node:
    def __init__(self,data):
        self.data = data # 节点数据
        self.next = None # 代表指针，先给他给None

# 创建单链表
class SingleNode:

    def __init__(self):
        self.head = None # 先初始化一个头节点

    def is_empty(self):

        return self.head is None

    def get_length(self):
        cur = self.head
        length=0
        while cur is not None:
            length += 1
            cur = cur.next
        return length

    # 再链表头部加入一个节点
    def add_first(self,data):
        node = Node(data)
        node.next=self.head # 1、因为是再头部添加，所以让加入的这个data指针指向头部
        self.head = node # 2、然后再赋予node这个节点是代表 “头部”称号的

    # 在链表尾部添加节点
    def add_last(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    # 插入元素
    def inser_data(self,index,data):
        node = Node(data)
        if index <0 or index > self.get_length():
            return False

        elif index==0:
            self.add_first(data)
        elif index == self.get_length():
            self.add_last(data)

        else:
            cur = self.head
            count = 0

    # 本来是要再index中插入，现在先需要找到index的前面一位，让index的前面一位指针指向index这一位，
    #         然后再让index的指针指向最后一位
            while count < index-1:
                cur = cur.next
                count += 1

            # 跳出while循环，表明cur此时已经遍历到了要插入的index的前一位了

            # cur.next = node ---这个不能这样写，先让cur的指针指向新插入的node的话，要不然就会丢失掉cur的下一个节点
            node.next = cur.next  # cur此时还存储着下一个节点的信息，所以先让node等于cur的下一个节点，要不然会丢失下一个节点

            cur.next = node # 然后再让cure的指针指向新插入的 node节点


    def delete_node(self,data):
        cur = self.head
        pre = None # 先初始化当前节点cur的前面节点
        if self.head == data:
            self.head.next = self.head  # 删除的结点是头结点：这种情况就直接将头结点的称号给头结点的后继结点就可以了

        else:
            while cur.data != data: # 遍历，找出我们要删除的data值，cur.data表名要取出节点的data值进行比较
                pre = cur # cur的前面节点的pre
                cur = cur.next  # 表示cur始终是再pre的下一个节点
            pre.next = cur.next # 找到那个被删除的data后,也就是cur节点，直接让pre指向cur的下一个节点即可

    # 遍历链表
    def traversal(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    # 查找某一个节点是否存在
    def search_node(self,data):
        cur =self.head
        count = 0
        while cur is not None:

            if cur.data == data:
                return True
            else:
                cur = cur.next
        return False




if __name__ == '__main__':
    lists = SingleNode()
    lists.add_first(2)
    lists.add_first(1)
    lists.add_last(4)
    lists.inser_data(2, 3)
    # lists.traversal()
    # print(lists.get_length())

    lists.delete_node(4)
    lists.traversal()
    print(lists.search_node(4))
    lists.traversal()















