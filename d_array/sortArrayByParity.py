# -*- coding: utf-8 -*-
# 给定一个非负整数数组
# A，返回一个由
# A
# 的所有偶数元素组成的数组，后面跟
# A
# 的所有奇数元素。
#
# 你可以返回满足此条件的任何数组作为答案。
#
#
#
# 示例：
#
# 输入：[3, 1, 2, 4]
# 输出：[2, 4, 3, 1]
# 输出[4, 2, 3, 1]，[2, 4, 1, 3]
# 和[4, 2, 1, 3]
# 也会被接受。
# 提示：
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A or len(A) == 1:
            return A
        odd_pos = -1
        for index, i in enumerate(A):
            # 奇数不变
            if i % 2 == 1:
                if odd_pos == -1:
                    odd_pos = index
                continue
            # 偶数就与奇数做交换
            if i % 2 == 0 and index != odd_pos and odd_pos != -1:
                A[index], A[odd_pos] = A[odd_pos], A[index]
                odd_pos += 1
        return A


A = [0, 3, 1, 2, 4, 1, 0, 100, 100, 0]
print Solution().sortArrayByParity(A)
