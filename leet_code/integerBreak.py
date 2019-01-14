# coding:utf-8

# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
#
# 示例 1:
#
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 示例 2:
#
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 说明: 你可以假设 n 不小于 2 且不大于 58。

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            # let's say i = 8, we are trying to fill dp[8]:if 8 can only be broken into 2 parts,
            # the answer could be among 1 * 7, 2 * 6, 3 * 5, 4 * 4...
            # but these numbers can be further broken. so we have to compare 1 with dp[1], 7 with dp[7], 2 with dp[2], 6 with dp[6]...etc
            for j in range(1, i / 2 + 1):
                # use Math.max(dp[i],....)  so dp[i] maintain the greatest value
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
                print ("i:%d\tj:%d\tdp[%d]:%d" % (i, j, i, dp[i]))
        return dp[-1]

    def integerBreak1(self, n):
        if n <= 3:
            return n - 1
        dp = [0] * (n + 1)
        dp[2], dp[3] = 2, 3
        for i in range(4, n + 1):
            dp[i] = max(3 * dp[i - 3], 2 * dp[i - 2])
        return dp[-1]


print Solution().integerBreak1(51)
# Solution().integerBreak(8)
