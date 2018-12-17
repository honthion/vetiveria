# coding:utf-8

# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2]
#   [2,2],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        global out, s
        out = [[]]
        s = []

        def dfs(i):
            global out, s
            for j in range(i, len(nums)):
                s.append(nums[j])
                print s
                out.append(s[:])
                dfs(j + 1)
                s = s[:len(s) - 1]

        dfs(0)
        return out


nums = [1, 2, 3, 4, 5, 6]
ret = Solution().subsetsWithDup(nums)
for i in ret:
    print i
