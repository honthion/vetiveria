# -*- coding:utf-8 -*-
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        ori = range(1, 10)

        def dfs(depth, start, value_list):
            if len(value_list) == k and sum(value_list) == n:
                res.append(value_list)
            if depth == len(ori):
                return
            for i in range(start, len(ori)):
                dfs(depth + 1, i + 1, value_list + [ori[i]])

        dfs(0, 0, [])
        return res

    def combinationSum30(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res, arr, sum_val = [], [], 0

        def find_count(i, arr, sum_val):
            if len(arr) > k or sum_val > n:
                return
            if sum_val == n and len(arr) == k:
                res.append(arr)
                return
            for j in range(i + 1, 10):
                find_count(j, arr + [j], sum_val + j)

        find_count(0, arr, sum_val)
        return res


def test():
    return Solution().combinationSum30(3, 9)


res = test()
print res
