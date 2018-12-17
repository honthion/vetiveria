# -*-coding:utf-8 -*-
#  给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
class Solution(object):
    def subsets(self, nums):

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(depth, start, value_list):
            res.append(value_list)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth + 1, i + 1, value_list + [nums[i]])

        nums.sort()
        res = []
        dfs(0, 0, [])
        return res

    def subsets0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        global out, s
        s = []
        out = [[]]

        def dfs(i):
            global out, s

            for j in range(i, len(nums)):
                s.append(nums[j])

                out.append(s[:])

                dfs(j + 1)
                s = s[:len(s) - 1]

        dfs(0)

        return out


nums = [1, 2, 3]
print Solution().subsets(nums)
