# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        result = []

        def dfs(node):

            if node.left is None and node.right is None:
                result.append(node.val)
                return

            # internal node
            if node.left is not None:
                dfs(node.left)

            result.append(node.val)

            if node.right is not None:
                dfs(node.right)
        
        dfs(root)
        return result