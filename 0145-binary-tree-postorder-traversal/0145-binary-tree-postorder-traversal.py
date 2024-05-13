# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return None

        result = []

        def dfs(node):

            if node.left is None and node.right is None:
                result.append(node.val)
                return

            # internal node
            if node.left is not None:
                dfs(node.left)

            if node.right is not None:
                dfs(node.right)

            result.append(node.val)

        dfs(root)
        return result
        