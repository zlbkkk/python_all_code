# 输入: 1->2->3->NULL
# 输出: 3->2->1->NULL
# 题目给的条件：给你单链表的头节点head

def reverse(self,head):
    prev = None
    cur = head # 指向头部的节点1

    while cur:
        # 先用tmp保存头部节点的下一个节点的信息，
        # 因为反转时，我们会用第一个节点指向None，避免因为而丢失
        #  第二个节点
        tem = cur.next  #使tem 指向cur（1节点）的下一个节点2
        cur.next = prev #cur.next代表cur的下一个节点等于prev,即：使cur的下一个节点指向None，1-->None

        # prev，cur依次向后移动一个节点，继续下一次的指针反转
        prev = cur # 此时
        cur = tem
    return prev


def fanzhuan(head):

    pre=None
    cur =head

    while cur:
        tem =cur.next

        cur.next = pre

        pre =cur

        cur = tem

    return pre




















