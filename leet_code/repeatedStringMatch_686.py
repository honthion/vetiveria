class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = -(-len(B) // len(A))
        for i in range(2):
            if B in (A * (times + i)):
                return times + i
        return -1

# return t * (B in A*t) or (t+1) * (B in A*(t+1) ) or -1

A = "abcd"
B = "cdabcdab"
Solution().repeatedStringMatch(A, B)
