# 题目：
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# 思路：1、先判断两个链表是否都有值，如果只有一个链表有值，直接返回那个链表
#
#      2、l1和l2链表，将l1的第一个节点和l2的第一个节点比较，哪个小取哪一个，
#         然后在使用递归，小的那个链表的取值，要从下一个节点开始

#      3、在递归结束后，至多有一个链表是空的，因为链表是有序的，所以只需要把这个链表元素接在后面即可


# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1

        else:

            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
#
# 关于return L1的个人理解: 递归的核心在于,我只关注我这一层要干什么,返回什么,至于我的下一层(规模减1),我不管,我就是甩手掌柜.
#
# 好,现在我要merge L1,L2.我要怎么做?
#
# 显然,如果L1空或L2空,我直接返回L1或L2就行,这很好理解.
# 如果L1第一个元素小于L2的? 那我得把L1的这个元素放到最前面,至于后面的那串长啥样 ,我不管. 我只要接过下级员工干完活后给我的包裹, 然后把我干的活附上去(令L1->next = 这个包裹)就行
# 这个包裹是下级员工干的活,即merge(L1->next, L2)
# 我该返回啥?
#
# 现在不管我的下一层干了什么,又返回了什么给我, 我只要知道,假设我的工具人们都完成了任务, 那我的任务也就完成了,可以返回最终结果了
# 最终结果就是我一开始接手的L1头结点+下级员工给我的大包裹,要一并交上去, 这样我的boss才能根据我给它的L1头节点往下找,检查我完成的工作