class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        return len(s.split("\\s*"))


print Solution().countSegments("Hello, my name is John")

