

# 节点类：链表每一个节点有两个域，元素和指向下一个节点的链接
class Node:
    def __init__(self,elen):
        self.elen = elen  # 元素
        self.next = None # 指向下一个节点的链接，因为不知道指向谁，先为空


#调用示例 ：有多少个节点就调用多少次
# node = Node(100)

class SingleLinkList:
    def __init__(self,node=None):

#构造链表头部指针P，也就是链表头部的空域，从头部空域开始，P指向链表的下一个节点，。
        self._head = node  #  ----- >  这个node是指向上面Node类的实例，第一次调用Node时，创建的是链表的第一个元素，
                                       # 但是第一个元素没有一个连接指向他，所以要创建一个链接指向空元素，然后顺着这个链接就可以找到下面的元素

    def is_empty(self):
        # 链表是否为空
        return self._head == None

    def length(self):
        # 链表长度的函数

        # 遍历整个链表
        # cur游标用来移动遍历节点
        cur = self._head  # 游标等于head，让他从头开始
        count = 0
        while cur != None:
            count += 1
            cur = cur.next  # 使游标向右移动的代码
        return count

    def travel(self):
        # 遍历链表
        cur = self._head  # 刚开始让指针从头开始
        while cur != None:
            print(cur.elen,end=" ")
            cur = cur.next # 一直next，直到最后一位是否等于None

    def add(self,item):
        # 链表头部添加元素
        node = Node(item) # 1、node是新加的节点
        node.next = self._head # 2、self._head原本是指向后面的元素，现在让node.next指向self._head所指向的，然后看3
        self._head = node  # 3、然后让头部的空域指向新加的这个元素，这样就把元素给插入到了头部，并且链表不会断


    def append(self,item):
        # 链表尾部添加元素
        node = Node(item) # 增加一个节点

        # 3、这个if..else主要是为了处理链表刚开始就为空的情况
        if self.is_empty():
    # 1、如果链表为空，就不用遍历到最后，直接让他的指针指向这个新添加的节点，等价于向链表末尾添加节点了
            self._head = node
        else:
        # 2、如果链表开始就不为空，则让游标指向这个链表
            cur = self._head

            while cur.next != None: # 4、如果下一步的cur没有等于None，说明没到链表的最后
                cur = cur.next # 5、没到最后，就一直next

        # 6、代表到了最后之后，cur.next 为空，现在让他指向node，等于就是在后面增加了一个节点
            cur.next = node



    def insert(self, pose,item):
        # 指定位置添加元素
    # 这个if ...else是判断传入的索引值小于0或者大于链表长度的时候
        if pose <0:
            self.add(item)
        elif pose > (self.length()-1):
            self.append(item)
        else:
            # 以下是插入的索引值是正常的时候
            pre = self._head # 1、让这个指针从头部开始
            count = 0 # 2、记录pre的位置

        # 3、pose代表在哪个位置插入，这个是计算出在pose前面的那一位插入这个节点
            while count < (pose-1):
                count += 1
                pre=pre.next # 4、让pre这个指针不断向后移动

            node = Node(item) # 5、构造节点
    # 6、让node的空域指向pre下面的那个元素，pre.next才代表下一个元素，也就是新插入的这个元素指向pre的下一个元素，即：300这个元素
            node.next = pre.next
            pre.next = node # 7、 让pre这个元素的空域指向node




    def remove(self,item):
        # 删除节点
        cur = self._head #让指针从开头开始

    # 创建一个游标pre，目的是让这个游标跳过已经删除的节点，指向删除节点的下一个节点
        pre = None
        while cur != None:
            if cur.elen == item: # 这个if代表该元素是否等于要删除的元素
                if cur == self._head: #判断要删除的元素是否就是第一个元素
                    self._head =cur.next   #如果在头部 ，直接让头部元素指向第一个元素的下一个元素
                else:
                    pre.next = cur.next
                break

            else:  #这个else是找不到该元素，继续循环的分支
                pre = cur # cur指针先移动，pre指针，后面跟着移动，如果没找到那个删除的元素，让他们的指针相等
                cur = cur.next


    def search(self,item):
        # 查找节点是否存在
        cur = self._head # 让指针在开头
        while cur != None:
            if cur.elen == item:
                return True # 找到就返回 return True
            else:
                cur = cur.next
        return False #如果遍历完之后找不到就返回False





if __name__=="__main__":

    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(-1,9)
    ll.insert(2,100)
    ll.insert(18,200)
    ll.travel()

    ll.remove(100)
    ll.remove(9)

    ll.travel() # 9 8 100 1 2 3 4 5 6 200