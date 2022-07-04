# 题目：
#     给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
#     如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
#     您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#     示例：
#
#     输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
#     输出：7 -> 0 -> 8
#     原因：342 + 465 = 807


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)  #头结点，无存储，指向链表第一个结点
        node = head         #初始化链表结点
        carry = 0           #初始化 进一 的数
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry              # 对每一位求和
            carry = sum // 10                # 地板除，求进一（其为0或1）
            node.next = ListNode(sum % 10)   # 取余数，求本位结点
            if l1:                           # 求空否，防止出现无后继结点
                l1 = l1.next
            if l2:                           # 同上
                l2 = l2.next
            node = node.next                 # 更新指针
        if carry != 0:                       # 验证最后一位相加是否需 进一
            node.next = ListNode(1)
        return head.next         # 将之前的头节点指向链表，即可形成一个完整的链表





class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        #定义一个当前指针cur；和一个result，result用于最后结果，将result从头指向这个结果链表
        result = cur=ListNode()  # 创建一个空的节点
        remainder = 0 #进位项

        while l1 or l2: # 只要链表l1和l2有一个不为空，就继续遍历下去

            # 下main这两行：那个链表先为空了，就用0来不足这一位数，和另外一个链表相加
            x = l1.val if l1 else 0 # 能进入while也有可能 l1 或者l2是已经为空了，但是有一个还不为空
            y = l2.val if l2 else 0

            total = x+y+remainder

            # 这里是创造出一个个节点来,以第一次循环举例：开始cur是初始化再第一个节点，现在让他指向刚创建出来的下一个节点
            cur.next = ListNode(total%10) #调用ListNode创建节点，total%10表示超过10时，只留下余数，其他的是进位项
            remainder = total//10 # 表示进位项是多少

            # 防止某一链表已经为空，空链表.next会报错
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            cur = cur.next # 移动cur指针，以第一次循环为例：让他在第二个节点


        if remainder:  # 跳出循环，说明两个链表已经是空的了，已经遍历到最后了，现在看一下remainder还需不需要仅为
            cur.next = ListNode(remainder) # 进位项使用节点类 ListNode创建它

    # result初始化时是第一个头节点，他是和刚开始cur一样的，随着cur不断的往下建立链表，最后创建出来链表之后，让result指向下一个节点就可以把链表串起来了
        return result.next






















