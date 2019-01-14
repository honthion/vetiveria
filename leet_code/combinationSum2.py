# coding:utf-8
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]
# 理解不了
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [set() for i in xrange(target + 1)]
        dp[0].add(())
        for num in candidates:
            for t in xrange(target, num - 1, -1):
                for prev in dp[t - num]:
                    print "num:%d,t:%d,dp[%d]:%s,%s" % (num, t, t - num, str(dp[t - num]), str(dp[t]))
                    dp[t].add(prev + (num,))
                    print "--------> dp[%d]:%s" % (t, str(dp[t]))
        return list(dp[-1])

    def combinationSum20(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [set() for i in xrange(target + 1)]
        dp[0].add(())
        for num in candidates:
            for t in xrange(target, num - 1, -1):
                for prv in dp[t - num]:
                    dp[t].add(prv + (num,))
        return list(dp[-1])


candidates = [1, 2, 3, 4, 5, 6, 7, 8]
target = 8
print Solution().combinationSum2(candidates, target)
