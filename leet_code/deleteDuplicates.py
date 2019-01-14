# -*- coding: utf-8 -*-
# Definition for singly-linked d_list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        head_new = pre = None
        count = 0
        while head:
            if not head.next:
                if count == 0:
                    if pre:
                        pre.next = head
                    else:
                        head_new = head
                else:
                    if pre:
                        pre.next = None
                    else:
                        head_new = None
                break
            if head.val != head.next.val:
                if count == 0:
                    if pre:
                        pre.next = head
                        pre = pre.next
                    else:
                        head_new = pre = head
                count = 0
            else:
                count += 1
            head = head.next
        return head_new


def test1():
    head = None
    arr = [-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21, 23, -21, 5]
    arr = [1,1]
    head0 = None
    cirle_head = None
    for i in arr:
        if not head:
            head = ListNode(i)
            head0 = head
        else:
            p = ListNode(i)
            head.next = p
            head = p
    Solution().deleteDuplicates(head0)


test1()
