# coding:utf-8
# 给定一个整数数组# A，返回其中元素之和可被# K# 整除的（连续、非空）子数组的数目。
#
#
#
# 示例：
#
# 输入：A = [4, 5, 0, -2, -3, 1], K = 5
# 输出：7
# 解释：
# 有# 7# 个子数组满足其元素之和可被# K = 5
# 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
# 提示：
#
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
# 这个问题和之前的问题Leetcode 525：连续数组（超详细的解法！！！）和Leetcode 560：和为K的子数组（超详细的解法！！！）类似，我们还是使用累加和的做法。
# 同样，我们对于这种问题的关键就是找到对称点（也就是我们关心的是在字典中存什么的问题），由于这个问题是考虑元素之和可被K整除，所以我们通过字典去记录累加和%K的余数即可。
# 接着剩余的问题就和Leetcode 560：和为K的子数组（超详细的解法！！！）一模一样了。
#
# 同样考虑边界情况，也就是pre_sum%K==0的时候，此时一个好的处理办法就是在初始化dict的时候，添加{0:1}。


class Solution(object):

    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        count = [1] + [0] * K
        res = 0
        prefix = 0
        for a in A:
            prefix = (prefix + a) % K
            res += count[prefix]
            print count
            print "%d,%d,%d" % (a, prefix, res)
            count[prefix] += 1
        return res


A = [4, 5, 0, -2, -3, 1]
cnt = (Solution().subarraysDivByK(A, 5))
print cnt
