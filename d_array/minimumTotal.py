# coding:utf-8
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
# 说明：
#
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。


class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        ret = range(len(triangle))
        for index, i in enumerate(triangle):
            i[0] += ret[0]
            if index > 0:
                i[index] += ret[index - 1]
            if index > 1:
                for j in range(1, index):
                    i[j] += min(ret[j - 1], ret[j])
            ret[:] = i
            print ret

        return min(ret)

    def minimumTotal1(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        L = len(triangle)
        # res = 1e10
        if L == 1:
            return triangle[0][0]
        for i in range(1, L):
            for j in range(i + 1):
                left = 1e10 if j == 0 else triangle[i - 1][j - 1]
                mid = 1e10 if j == i else triangle[i - 1][j]
                # right = 1e10 if j >= i-1 else triangle[i-1][j+1]
                triangle[i][j] += min(left, mid)
                # if i == L-1 and triangle[L-1][j] < res:
                #     res = triangle[L-1][j]
        return min(triangle[-1])


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
triangle1 = [
    [-1],
    [3, 2],
    [-3, 1, -1]]

print Solution().minimumTotal(triangle)
