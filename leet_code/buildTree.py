# coding:utf-8

# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        inorder_index = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorder_index + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)

        return root

    def buildTree0(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None
        hm = {}
        for index, i in enumerate(inorder):
            hm[i] = index

        def build_tree_post_in(post_end, in_start, in_end):
            if in_start == in_end:
                return None
            root = TreeNode(postorder[post_end - 1])
            i = hm[postorder[post_end - 1]]
            root.right = build_tree_post_in(post_end - 1, i + 1, in_end)
            root.left = build_tree_post_in(post_end - 1 - (in_end - i - 1), in_start, i)
            return root

        root = build_tree_post_in(len(postorder), 0, len(inorder))
        return root

    def buildTreePre(self, preorder, inorder):
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None

        hm = {}
        for index, i in enumerate(inorder):
            hm[i] = index

        def build_tree_pre_in(pre_start, in_start, in_end):
            if in_start == in_end:
                return None
            root = TreeNode(preorder[pre_start])
            i = hm[preorder[pre_start]]
            root.right = build_tree_pre_in(pre_start + i + 1 - in_start, i + 1, in_end)
            root.left = build_tree_pre_in(pre_start + 1, in_start, i)
            return root

        return build_tree_pre_in(0, 0, len(inorder))

    def buildTreePre1(self, preorder, inorder):
        if inorder:
            root_val = preorder.pop(0)
            inorder_index = inorder.index(root_val)
            root = TreeNode(root_val)
            root.left = self.buildTreePre1(preorder, inorder[0:inorder_index])
            root.right = self.buildTreePre1(preorder, inorder[inorder_index + 1:])

            return root


def printRoot(root):
    if not root:
        return
    print root.val
    printRoot(root.left)
    printRoot(root.right)


# inorder = [9, 3, 15, 20, 7]
# postorder = [9, 15, 7, 20, 3]
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = Solution().buildTreePre(preorder, inorder)

printRoot(root)
