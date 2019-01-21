# coding:utf-8
# 给定一个二进制数组, 找到含有相同数量的0和1的最长连续子数组（的长度）。
#
#
#
# 示例
# 1:
#
# 输入: [0, 1]
# 输出: 2
# 说明: [0, 1]
# 是具有相同数量0和1的最长连续子数组。
# 示例
# 2:
#
# 输入: [0, 1, 0]
# 输出: 2
# 说明: [0, 1](或[1, 0])
# 是具有相同数量0和1的最长连续子数组。

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = max_length = 0
        arr = {0: 0}
        for index, i in enumerate(nums,1):
            cnt += i > 0 and 1 or -1
            if cnt in arr:
                max_length = max(max_length, index - arr[cnt])
            else:
                arr[cnt] = index
        return max_length


nums = [0, 1, 0]
nums = [0, 0, 0, 0, 1, 1]
nums = [0, 0, 1, 0, 0, 0, 1, 1]
nums = [0, 1, 1, 0, 1, 1, 1, 0]
print Solution().findMaxLength(nums)
