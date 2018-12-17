# -*- coding:utf-8 -*-

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
#
# 输入: [3,4,5,1,2]
# 输出: 1
# 示例 2:
#
# 输入: [4,5,6,7,0,1,2]
# 输出: 0


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = (start + end) / 2
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid
        return nums[start]


nums = [2,1]

print Solution().findMin(nums)
