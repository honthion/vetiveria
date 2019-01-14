# -*- coding: utf-8 -*-
# 给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
#
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。
#
# 示例 1:
#
# 输入: [4,2,3]
# 输出: True
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
# 示例 2:
#
# 输入: [4,2,1]
# 输出: False
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
# 说明:  n 的范围为 [1, 10,000]。
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # i, n, count = 0, len(nums), 0
        # for j in range(n - 1):
        #     if nums[j + 1] < nums[j]:
        #         i = j
        #         count += 1
        # if count == 0:
        #     return True
        # elif count > 1:
        #     return False
        # else:
        #     if i == 0 or i == n - 2 or nums[i + 1] >= nums[i - 1] or nums[i + 2] >= nums[i]:
        #         return True
        #     else:
        #         return False

        l = len(nums)
        ans = 0
        for i in range(1, l):
            if nums[i] < nums[i - 1]:
                ans += 1
                if ans == 1:
                    if (i + 1 < l and nums[i + 1] < nums[i - 1]) and (i - 2 >= 0 and nums[i] < nums[i - 2]):
                        return False
                if ans == 2:
                    return False
        return True


# nums = [1, 3, 4, 2, 5]
# nums = [4, 2, 1]
# nums = [1, 2, 3, 5, 4]
nums = [1, 2, 5, 3, 4]
# nums = [3, 4, 2, 3]
print Solution().checkPossibility(nums)
