

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
        self._head = node  #  ----- >  如果传入node，那就指向node节点，如果不传，就指向None，
                                       # 但是第一个元素没有一个连接指向他，所以要创建一个链接指向空元素，然后顺着这个链接就可以找到下面的元素
        if node != None:
            node.next = node #因为是单项循环链表，所以最末尾的元素，要反向指回开头的节点，现在是传进一个节点，那就应该指向它本身


    def is_empty(self):
        # 链表是否为空
        return self._head == None

    def length(self):
        # 链表长度的函数

        if self.is_empty():
            return 0

        # 遍历整个链表
        # cur游标用来移动遍历节点
        cur = self._head  # 游标等于head，让他从头开始
        count = 1
        while cur.next != self._head :
            count += 1
            cur = cur.next  # 使游标向右移动的代码
        return count

    def travel(self):
        # 遍历链表

        #空链表的情况
        if self.is_empty():
            return

        cur = self._head  # 刚开始让指针从头开始
        while cur.next != self._head:  #因为最后一个节点指向第一个节点
            print(cur.elen,end=" ")
            cur = cur.next # 一直next，直到最后一位是否等于None
        print(cur.elen)

    def add(self,item):
        # 链表头部添加元素
        node = Node(item)  # 1、node是新加的节点

        if self.is_empty(): #如果刚开始是空链表情况，那就是插入的节点是第一个节点
            self._head = node
        else:

            # 因为尾部节点要指向头部节点，所以在头部增加了节点只之后，要让尾部的节点指向这个新加的节点

            cur = self._head
            while cur.next != self._head: # 这个循环时要找到尾部节点
                cur = cur .next

            node.next = self._head  # self._head原本是指向后面的元素，现在让node.next指向self._head所指向的，
            self._head = node # P指向新加入到头部的node元素
            cur.next = self._head  # 尾部元素指向头部元素


    def append(self,item):
        # 链表尾部添加元素
        node = Node(item) # 增加一个节点

        # 3、这个if..else主要是为了处理链表刚开始就为空的情况
        if self.is_empty():
    # 1、如果链表为空，就不用遍历到最后，直接让他的指针指向这个新添加的节点，等价于向链表末尾添加节点了
            self._head = node

            node.next = self._head
        else:
        # 2、如果链表开始就不为空，则让游标指向这个链表
            cur = self._head

            while cur.next != self._head: # 4、如果下一步的cur没有等于None，说明没到链表的最后
                cur = cur.next # 5、没到最后，就一直next

        # 6、代表到了最后之后，cur.next 为空，现在让他指向node，等于就是在后面增加了一个节点
            node.next = self._head  # 尾部元素返回来指向头部元素
            cur.next = node #原来的尾部节点，指向新加到尾部的节点




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
        while cur.next != self._head:
            if cur.elen == item: # 这个if代表该元素是否等于要删除的元素
                if cur == self._head: #判断要删除的元素是第一个元素的情况
                    rear = self._head # 建立新的指针
                    while rear.next != self._head:
                        rear = rear.next

                    #以下是：找到了最后一个节点
                    self._head = cur.next # 因为要删除的是头部元素，所以让P指向了头部元素所指向的下一个元素
                    rear.next = self._head # 尾部元素指向头部元素

                else: # else代表是在中间节点找到的
                    pre.next = cur.next   # 让pre的空域指向 cur 所指向的下一个元素
                return

            else:  #这个else是找不到该元素，继续循环的分支
                pre = cur # cur指针先移动，pre指针，后面跟着移动，如果没找到那个删除的元素，让他们的指针相等
                cur = cur.next

        if cur.elen == item: # 这个if是如果要删除的是尾部节点的情况，因为这个cur.next != self._head条件尾部元素不会被循环到,上面跳出while循环即代表已经到了尾部节点
            if cur == self._head:  # 链表只有一个节点的情况，也就是头尾节点相等的情况就是只有一个节点
                self._head = None  # 继上面哪一个if，删除唯一的节点，就是让self._head指向None即可
            else:
                pre.next = cur.next


    def search(self,item):
        # 查找节点是否存在

        # 链表为空时,直接返回
        if self.is_empty():
            return False

        cur = self._head # 让指针在开头
        while cur.next != self._head:  #1、这个条件会缺少最后一个元素遍历不到，因为最后一个元素的cur.next就是等于头部，就不会进去循环，这样最后一个元素就不会被遍历
            if cur.elen == item:
                return True # 找到就返回 return True
            else:
                cur = cur.next
        if cur.elen == item: # 继承1 ：因为最后一个元素遍历不到，这里要加特别判断
            return True


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
    ll.remove(200)

    ll.travel() # 9 8 100 1 2 3 4 5 6 200