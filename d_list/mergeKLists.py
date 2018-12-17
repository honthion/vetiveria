# -*- coding: utf-8 -*-
# Definition for singly-linked d_list.
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# #
# # 示例:
# #
# # 输入:
# # [
# #   1->4->5,
# #   1->3->4,
# #   2->6
# # ]
# # 输出: 1->1->2->3->4->4->5->6


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    if not lists:
        return lists
    l0 = []
    while True:
        min = minObj(lists)
        if not min:
            break
        l0.append(min.val)
    return sort_list(l0)


# 通过快排的方式来解决
def sort_list(lists):
    l0 = []
    # 获取所有元素
    for i in lists:
        while True:
            val = i.val
            l0.append(val)
            i = i.next
            if not i:
                break
    # 快速排序
    quick_sort(l0, 0, len(l0))
    return l0


def quick_sort(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        quick_sort(lst, lo, p)
        quick_sort(lst, p + 1, hi)
    return


def partition(lst, lo, hi):
    pivot = lst[hi - 1]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[hi - 1] < lst[i + 1]:
        lst[i + 1], lst[hi - 1] = lst[hi - 1], lst[i + 1]
    return i + 1


# 这个方法有点慢
def minObj(lists):
    min = None
    position = 0
    for index, i in enumerate(lists):
        if i:
            min = i
            position = index
            break
    if not min:
        return None

    for index, i in enumerate(lists):
        if i and i.val <= min.val:
            min = i
            position = index

    lists[position] = lists[position].next
    return min


def test():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(4)
    l2.next.next = ListNode(5)
    l2.next.next.next = ListNode(8)

    l3 = ListNode(0)
    l3.next = ListNode(9)

    l = []
    l.append(l1)
    l.append(l2)
    l.append(l3)

    print mergeKLists(l)


def test1():
    l0 = [999, 5, 9, 3, 2, 6, 7]
    quick_sort(l0, 0, len(l0))
    print l0


test1()
