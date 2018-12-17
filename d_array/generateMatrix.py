# -* coding:utf-8 *-
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例:
#
# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res, low = [], n * n + 1
        while low > 1:
            low, high = low - len(res), low
            res1 = zip(*res[::-1])
            res = [list(range(low, high))] + list(res1)
            print res
        return res


def test():
    for i in Solution().generateMatrix(5):
        print i


# 转置后还原
def test_zip():
    a = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16)]
    a1 = zip(*a)
    for i in a1:
        print i
    a2 = list(a1)
    a3 = zip(*a2)
    for i in a3:
        print i


test_zip()
