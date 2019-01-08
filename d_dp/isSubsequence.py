# congding:utf-8

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = j = 0
        lens = len(s)
        lent = len(t)
        while j < lent and lens:
            if s[i] == t[j]:
                i += 1
            j += 1
            if i == lens:
                return True
        return False

    def isSubsequence0(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pos = 0
        for i in s:
            if t.find(i, pos) != -1:  ##从下标1开始，查找在字符串里第一个出现的子串：
                pos = t.index(i, pos) + 1
            else:
                return False
        return True


b = Solution().isSubsequence('', 'ahbcded')
print b
