# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bottom up dfs
def dfs(node, dia):

    # common area
    # leaf node
    if node.left is None and node.right is None:
        return 1
    # internal node
    leftDia, rightDia = 0, 0

    if node.left is not None:
        # leftDia += 1
        leftDia = dfs(node.left, dia)
        # dia[0] = leftDia + rightDia 

    if node.right is not None:
        # rightDia += 1
        rightDia = dfs(node.right, dia)
        # dia[0] = rightDia + leftDia 

    # before returning
    dia[0] = max((leftDia + rightDia), dia[0]) 

    # return area
    if leftDia >= rightDia:
        # dia[0] = leftDia + rightDia
        return leftDia + 1
    else:
        # dia[0] = rightDia + leftDia
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
        dia = [0]

        dfs(root, dia)
        return dia[0]
        