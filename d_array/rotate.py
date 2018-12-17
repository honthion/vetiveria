# -*-coding:utf-8 -*-
# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。
#
# 说明：
#
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
#
# 示例 1:
#
# 给定
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 示例 2:
#
# 给定
matrix1 = [
    [00, 01, 02, 03],
    [10, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33]
]


#
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(0, length / 2):
            for j in range(i, length - 1 - i):
                tem = matrix[i][j]
                matrix[i][j] = matrix[length - 1 - j][i]
                matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
                matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
                matrix[j][length - 1 - i] = tem

    def rotate0(self, matrix):
        length = len(matrix)
        for i in range(length):
            for j in range(i + 1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(length):
            matrix[i].reverse()

    def rotate1(self, matrix):
        matrix[:] = map(list, zip(*matrix[::-1]))


Solution().rotate1(matrix1)
for i in matrix1:
    print i
