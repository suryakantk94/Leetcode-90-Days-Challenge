# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(node, result, stack):
    
    if node is None:
        return
    
    stack.append(str(node.val))

    if node.left is None and node.right is None:
        # stack.append(str(node.val))
        result.append("->".join(stack))
        return

    if node.left is not None:
        # stack.append(str(node.left.val))
        dfs(node.left, result, stack)
        stack.pop()

    if node.right is not None:
        # stack.append(str(node.right.val))
        dfs(node.right, result, stack)
        stack.pop()

    # stack.pop()

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []

        result = []
        stack = []
        dfs(root, result, stack)
        return result


        