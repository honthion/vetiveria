# -*- coding:utf-8-*-
# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
#
# 示例 1:
#
# 输入: [2,2,3,4]
# 输出: 3
# 解释:
# 有效的组合是:
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
# 注意:
#
# 数组长度不超过1000。
# 数组里整数的范围为 [0, 1000]。


class Solution(object):

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(2, len(nums)):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    result += r - l
                    r -= 1
                else:
                    l += 1
        return result


print Solution().triangleNumber([2, 2, 3, 4])
