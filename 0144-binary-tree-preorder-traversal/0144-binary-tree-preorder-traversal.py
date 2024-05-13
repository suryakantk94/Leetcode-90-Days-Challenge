# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(node, result):

    # common area
    result.append(node.val)
    # leaf node
    if node.left is None and node.right is None:
        return

    # internal node
    if node.left is not None:
        dfs(node.left, result)

    if node.right is not None:
        dfs(node.right, result)


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        result = []
        dfs(root, result)

        return result