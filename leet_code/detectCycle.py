# -*- coding: utf-8 -*-
# Definition for singly-linked d_list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 环形链表 II
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 说明：不允许修改给定的链表。
#
# 进阶：
# 你是否可以不用额外空间解决此题？

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


# 在环上相遇后，记录第一次相遇点为Pos，之后指针slow继续每次走1步，fast每次走2步。在下次相遇的时候fast比slow正好又多走了一圈，也就是多走的距离等于环长。
@staticmethod
def circle_len(head):
    head0 = slow = fast = head
    slow_len = 0
    start_count = False
    meet_count = 0
    join_head = None
    while slow and fast and fast.next:
        slow0 = slow = slow.next
        fast = fast.next.next
        if slow is fast:
            start_count = True
            meet_count += 1
            join_head = join_point(head0, slow0)
        if meet_count == 2:
            break
        if start_count:
            slow_len += 1
    return slow_len, join_head

#https://www.cnblogs.com/xudong-bupt/p/3667729.html
# 第一次碰撞点Pos到连接点Join的距离=头指针到连接点Join的距离，因此，分别从第一次碰撞点Pos、头指针head开始走，相遇的那个点就是连接点。
def join_point(head, slow):
    join_head = None
    while True:
        if head is slow:
            join_head = head
            break
        head = head.next
        slow = slow.next
    return join_head


def test():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l2 = ListNode(3)
    l2.next = ListNode(5)
    l2.next.next = ListNode(7)
    l3 = ListNode(6)
    l1.next.next = l2
    l2.next.next.next = l3
    # l3.next = l2
    r1 = l1
    r2 = l1
    arr = []
    while True:
        if not r1 or not r1.next or not r2 or not r2.next or not r2.next.next:
            print "l1 not  circle."
            break
        arr.append(r1)
        r1 = r1.next
        r2 = r2.next.next
        if r1 == r2:
            print "l1 is circle."
            break


# 当变量是数字、字符串、元组，列表，字典时，is和==都不相同， 不能互换使用！当比较值时，要使用==，比较是否是同一个内存地址时应该使用is。当然，开发中比较值的情况比较多。
def test1():
    head = None
    arr = [-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21, 23, -21, 5]
    arr = [1, 2, 3, 4, 5, 6, 10, 11, 7, 8, 9]
    head0 = None
    cirle_head = None
    for i in arr:
        if not head:
            head = ListNode(i)
            head0 = head
        else:
            p = ListNode(i)
            if 5 == i:
                cirle_head = p
            head.next = p
            head = p
    head.next = cirle_head
    head = head0
    # l3.next = l2
    fast = slow = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True, join_point(head, slow)
    return False, None


# 标准答案
def s0(head):
    fast, slow, loop = head, head, False
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            loop = True
            break

    if not loop:
        return None

    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast


circlr, head = test1()
print circlr
print head.val
