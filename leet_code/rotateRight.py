# -*- coding: utf-8 -*-
#  Definition for singly-linked d_list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k < 1:
            return head
        len_count = 1
        save = head
        while True:
            if not head.next:
                head.next = save
                break
            head = head.next
            len_count += 1
        prev = None
        cnt = len_count - k % len_count
        while cnt >= 0:
            prev = head
            head = head.next
            cnt -= 1
        prev.next = None
        return head


def test1():
    head = None
    arr = [-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21, 23, -21, 5]
    arr = [1, 2, 3, 4, 5]
    arr = [1, 2]
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
    p = Solution().rotateRight(head0, 2)
    print p.val


test1()
