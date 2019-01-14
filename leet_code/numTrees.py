# coding:utf-8
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:  BST's (binary search trees)
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# 二叉搜索树
# 二叉查找树（英语：Binary Search Tree），也称为二叉搜索树、有序二叉树（ordered binary tree）或排序二叉树（sorted binary tree），是指一棵空树或者具有下列性质的二叉树：
#
# 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
# 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
# 任意节点的左、右子树也分别为二叉查找树；
# 没有键值相等的节点。



class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0] * (n + 1)
        arr[0] = arr[1] = 1
        for i in xrange(2, n + 1):
            for j in xrange(1, i + 1):
                arr[i] += arr[j - 1] * arr[i - j]
        print arr[-1]


Solution().numTrees(1)
Solution().numTrees(2)
Solution().numTrees(3)
Solution().numTrees(4)
