# -*- coding: utf-8 -*-
# Definition for singly-linked d_list.
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # 参数不合法，返回空list
    if not l1:
        return l1
    if not l2:
        return l2
    # 取值
    s1 = get_num_sum(l1)
    s2 = get_num_sum(l2)
    s3 = s1 + s2
    return get_list_node(s3)


# 获取一个数的ListNode
def get_list_node(s3):
    head = ListNode(s3 % 10)
    f1 = head
    s3 = s3 / 10
    while True:
        if s3 == 0:
            break
        f1.next = ListNode(s3 % 10)
        f1 = f1.next
        s3 = s3 / 10
    return head


# 单个链表求和
def get_num_sum(l1):
    if not l1:
        return 0
    i = 0
    s1 = 0
    while True:
        next_node = l1
        val = next_node.val
        s1 = s1 + pow(10, i) * val
        i = i + 1
        l1 = next_node.next
        if not l1:
            break
    return s1


# 测试用例
def test():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    add_two_numbers(l1, l2)


test()
