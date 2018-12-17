# coding:utf-8

# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
# 示例:
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p, n, output = 1, len(nums), []
        # 先左边向右边乘
        for i in range(n):
            output.append(p)
            p *= nums[i]
        p = 1
        # 再右边向左边乘
        for i in range(n - 1, -1, -1):
            output[i] *= p
            p *= nums[i]
        return output


nums = [1, 2, 3, 4]
# print Solution().productExceptSelf(nums)

print range(4, -1, -1)
