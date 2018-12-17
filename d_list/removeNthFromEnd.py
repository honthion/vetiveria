# -*- coding: utf-8 -*-
# Definition for singly-linked d_list.
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if not head:
        return
    if n < 1:
        return
    # 求出链表的长度
    head_0 = head
    size = 0
    while True:
        next = head.next
        size = size + 1
        if not next:
            break
        head = next
    print size
    if n > size:
        return
    count = 0
    head = head_0
    while True:
        if 0 == size - n:
            return head.next
        if count+1 == size - n:
            head.next = head.next.next
            return head_0
        else:
            if n == 1 and 2 == size - count:
                head.next = None
                return head_0
            head = head.next
        count = count + 1


def test():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(5)
    print removeNthFromEnd(l1, 4)


test()
