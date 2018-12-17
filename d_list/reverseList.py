# -*- coding: utf-8 -*-
# Definition for singly-linked d_list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = None
        curr = head
        h = head
        # 用的循环
        while curr:
            h = curr
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return h

    @staticmethod
    def recurse(head, new_head):  # head为原链表的节点头，new_head为反转后链表的节点头
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 如果链表为空或者链表中只有一个元素
        if not head or not head.next:
            return head
        else:
            # 先反转后面的链表，走到链表的末端结点
            new_head = Solution.recurse(head.next, new_head)
            # 再将当前节点设置为后面节点的后续节点
            head.next.next = head
            head.next = None
            return new_head




def test():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    # l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(4)
    # l1.next.next.next.next = ListNode(5)
    new_head = None
    p = Solution().recurse(l1, new_head)
    while p:
        print p.val
        p = p.next


test()
