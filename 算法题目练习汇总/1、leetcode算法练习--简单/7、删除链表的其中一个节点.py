"""如果我们要在链表中删除一个节点，一般的操作是：
    1、 修改要删除节点的上一个节点的指针
    2、将该指针指向要删除节点的下一个节点

但是现在只传进一个要删除的节点，我们完全不知道上一个节点是哪一个，
所以：比如[4, 5, 1, 9], 要删除节点5,

思路：
    将要删除的节点的下一个节点的值赋值给要删除的节点，即：将1赋值给5，
    代码： node.val = node.next.val
    赋值后：[4, 1, 1, 9], 这样一来我们就可以随便删掉哪一个节点都是：[4, 1, 9]
    了，删除，也就是把要删除的节点的指向，指向他的下下个节点：
    node.next = node.next.next

此思路，在“题目中指明了「给定的节点为非末尾节点」
且「链表至少包含两个节点」”的条件下可以使用
"""

# 解题思路：
    # 让当前节点成为下一个节点
    # 然后跳过下一个节点，这样就能将要删除的节点个替换掉

# 原来是：[4, 5, 1, 9] ， node.val = node.next.val后是 ：[4, 1, 1, 9]
# node.next = node.next.next 然后是： [4, 1, 9]

# 首先要定义一个链表节点类
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


print(abs(-23))