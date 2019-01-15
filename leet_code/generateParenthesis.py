class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generate(p, left, right, parent=[]):
            if left: generate(p + "(", left - 1, right)
            if right > left: generate(p + ")", left, right - 1)
            if not right: parent += p,
            return parent
        return generate("", n, n)

    def generateParenthesis1(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left - 1, right)
            if right > left: generate(p + ')', left, right - 1)
            if not right:    parens += p,
            return parens

        return generate('', n, n)

print Solution().generateParenthesis(3)
# print Solution().generateParenthesis1(3)
