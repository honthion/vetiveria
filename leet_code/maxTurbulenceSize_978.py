class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        if len(A) == 1:
            return 1
        max_length = 1
        cur_length = 1
        max_length_1 = 1
        cur_length_1 = 1
        tag = True
        for i in xrange(0, len(A) - 1):

            if (A[i] < A[i + 1] and tag) or (A[i] > A[i + 1] and not tag):
                cur_length += 1
                max_length = max(max_length, cur_length)
            else:
                cur_length = 1
            if (A[i] < A[i + 1] and not tag) or (A[i] > A[i + 1] and tag):
                cur_length_1 += 1
                max_length_1 = max(max_length_1, cur_length_1)
            else:
                cur_length_1 = 1
            tag = not tag
        return max(max_length, max_length_1)

    def maxTurbulenceSize0(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 2:
            return len(A)
        ret = [A[i] - A[i + 1] for i in xrange(len(A) - 1)]
        me = 1
        cur_max = 0
        for i in xrange(1,len(ret)):
            if ret[i - 1] * ret[i]<0:
                me += 1
            else:
                me =1
                cur_max = max(me,cur_max)
        return cur_max +1


A = [9, 4, 2, 10, 7, 8, 8, 1, 9]
A = [4, 8, 12, 16]
A = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
A = [100, 100, 100]
print Solution().maxTurbulenceSize(A)
