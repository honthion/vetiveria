# -*- coding: utf-8 -*-
# Definition for singly-linked d_list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
#
# 示例 :
#
# 给定这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
# 说明 :
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


class Solution(object):

    # 返回
    @staticmethod
    def reverse_list(head, k):
        i = 1
        head_old = head
        while i < k:
            if not head or not head.next:
                return head_old
            head = head.next
            i += 1
        head.next = None
        return Solution.revers(head_old, None)

        pass

    @staticmethod
    def revers(head, new_head):
        if not head or not head.next:
            return head
        else:
            new_head = Solution.revers(head.next, new_head)
            head.next.next = head
            head.next = None
            return new_head

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k <= 1:
            return head
        arr = []
        arr1 = []
        i = 0
        while head:
            if i % k == 0:
                arr.append(head)
            head = head.next
            i += 1
        for i in arr:
            p = Solution.reverse_list(i, k)
            arr1.append(p)
        head_new = arr1[0]
        tail = None
        for index, i in enumerate(arr1):
            if tail:
                tail.next = i
            while i:
                if not i or not i.next:
                    tail = i
                    break
                i = i.next

        return head_new


l1 = ListNode(2)
l1.next = ListNode(4)
l2 = ListNode(3)
l2.next = ListNode(5)
l3 = ListNode(6)
l1.next.next = l2
l2.next.next = l3


def test():
    p1 = Solution().reverse_list(l1, 2)
    p2 = Solution().reverse_list(l3, 2)

    while p1:
        print p1.val
        p1 = p1.next
    print "----------------------"
    while p2:
        print p2.val
        p2 = p2.next


def test1():
    p = Solution().reverseKGroup(l1, 3)
    while p:
        print p.val
        p = p.next


test1()
