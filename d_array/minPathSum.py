# coding:utf-8

# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]


# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return None
        m, n = len(grid), len(grid[0])

        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]


print Solution().minPathSum(grid)
