class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A or not B:
            return False
        if len(A) != len(B):
            return False
        if A == B and len(set(A)) < len(A):
            return True
        diff = [(a, b) for a, b in zip(A, B) if a != b]
        return len(diff) == 2 and diff[0] == diff[1][::-1]


A = "aaaaaaabc"
B = "aaaaaaacb"
print Solution().buddyStrings(A, B)
A = ""
B = "aa"
print Solution().buddyStrings(A, B)
A = "ab"
B = "ba"
print Solution().buddyStrings(A, B)
A = "ab"
B = "ab"
print Solution().buddyStrings(A, B)
A = "aa"
B = "aa"
print Solution().buddyStrings(A, B)
