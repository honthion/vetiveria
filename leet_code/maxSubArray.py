# coding:utf-8
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maxx = float('-inf')
        # for i in xrange(1, len(nums)):
        #     nums[i] = max(0, nums[i - 1]) + nums[i]
        #     maxx = max(maxx, nums[i])
        # return maxx

        sums = 0
        maxsum = nums[0]
        for num in nums:
            if sums < 0:
                sums = num
            else:
                sums += num
            maxsum = max(maxsum, sums)
        return maxsum


A = [1, 2]

print Solution().maxSubArray(A)
