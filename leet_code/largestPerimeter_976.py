class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        B = sorted(A)
        for i in range(len(A)-1, 1, -1):
            if B[i] - B[i - 1] < B[i - 2]:
                return B[i] + B[i - 1] + B[i - 2]
        return 0


A = [3, 6, 2, 3]
print Solution().largestPerimeter(A)
