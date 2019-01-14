# coding:utf-8
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
#
# 示例：
#
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 说明:
#
# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums:
            self.accu += [self.accu[-1] + num]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j + 1] - self.accu[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0, 2)
print param_1
