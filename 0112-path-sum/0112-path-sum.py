# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Top down DFS 
# requires additional parameters in the function call

# def dfs(node, targetSum, flag):
#     # leaf node
#     if node.left is None and node.right is None:
#         if targetSum == node.val:
#             flag[0] = True

#     # internal node worker
#     if node.left is not None:
#         dfs(node.left, targetSum - node.val, flag)

#     if node.right is not None:
#         dfs(node.right, targetSum - node.val, flag)

# Bottom up DFS
def dfs(node, targetSum):

    # leaf node
    if node.left is None and node.right is None:
        if node.val == targetSum:
            return True
        return False

    # internal node worker
    bleft, bright = False, False
    if node.left is not None:
        bleft = dfs(node.left, targetSum-node.val)

    if node.right is not None:
        bright = dfs(node.right, targetSum-node.val)

    return bleft or bright

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        # do a dfs traversal to reach all the nodes vertically one by one

        # handle null tree
        if not root:
            return False

        # setup a flag for Top Down DFS
        # flag = [False]
        # dfs(root, targetSum, flag)

        # for Bottom up DFS
        return dfs(root, targetSum)