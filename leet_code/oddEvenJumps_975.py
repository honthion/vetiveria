class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cur_max_min = A[-1]
        cnt = 1
        min_step = True

