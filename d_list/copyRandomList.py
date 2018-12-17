# -*- coding: utf-8 -*-
# Definition for singly-linked d_list with a random pointer.
# 复制带随机指针的链表
#
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
#
# 要求返回这个链表的深度拷贝。
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        save = head
        # 拷贝一份
        while head:
            new = RandomListNode(head.label)
            new.next = head.next
            head.next = new
            head = new.next
        # 修改拷贝的随机指针
        head = save
        while head:
            p = head.random
            if p:
                head.next.random = p.next
            head = head.next.next
        # 将拷贝拧出来
        head = new_head = save.next
        head_old = save
        while head:
            if not head.next:
                head.next = None
                save.next = None
                break
            else:
                save.next = save.next.next
                save = save.next
                head.next = head.next.next
                head = head.next

        return new_head, head_old


def test1():
    head = None
    arr = [-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21, 23, -21, 5]
    arr = [1, 9]
    head0 = None
    cirle_head = None
    for i in arr:
        if not head:
            head = RandomListNode(i)
            head0 = head
        else:
            p = RandomListNode(i)
            head.next = p
            head = p
    Solution().copyRandomList(head0)


test1()
