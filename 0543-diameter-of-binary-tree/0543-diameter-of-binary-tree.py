# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bottom up dfs
def dfs(node, globalDia):

    # common area
    # leaf node
    if node.left is None and node.right is None:
        return 1

    # internal node
    leftDia, rightDia = 0, 0

    if node.left is not None:
        leftDia = dfs(node.left, globalDia)
        # localDiameter = leftDia + rightDia

    if node.right is not None:
        rightDia = dfs(node.right, globalDia)
        # localDiameter = leftDia + rightDia

    # before returning
    localDiameter = leftDia + rightDia
    globalDia[0] = max((localDiameter), globalDia[0]) 

    # globalDia[0] = max((leftDia + rightDia), globalDia[0]) 

    # return area
    if leftDia >= rightDia:
        # localDiameter = leftDia + rightDia
        return leftDia + 1
    else:
        # localDiameter = leftDia + rightDia
        return rightDia + 1
    


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # handle null tree
        if not root:
            return 0
        globalDia = [0]

        dfs(root, globalDia)
        return globalDia[0]
        
