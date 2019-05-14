# coding:utf-8
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 说明 :
#
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
# 论坛上大家比较推崇的其实是这种解法，用一个哈希表来建立连续子数组之和跟其出现次数之间的映射，初始化要加入{0,1}这对映射，
# 这是为啥呢，因为我们的解题思路是遍历数组中的数字，用sum来记录到当前位置的累加和，
# 我们建立哈希表的目的是为了让我们可以快速的查找sum-k是否存在，即是否有连续子数组的和为sum-k，
# 如果存在的话，那么和为k的子数组一定也存在，这样当sum刚好为k的时候，那么数组从起始到当前位置的这段子数组的和就是k，
# 满足题意，如果哈希表中事先没有m[0]项的话，这个符合题意的结果就无法累加到结果res中，这就是初始化的用途。
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {0: 1}
        res = s = 0
        for n in nums:
            s += n
            res += sums.get(s - k, 0)
            sums[s] = sums.get(s, 0) + 1
        return res