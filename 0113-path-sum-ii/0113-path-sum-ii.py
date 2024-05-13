# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Top down DFS
def dfs(node, target, result, slate):

    # common area
    # add the info to pass to the child
    slate.append(node.val)

    # leaf node
    if node.left is None and node.right is None:
        if target == node.val:
            # slate.append(node.val)
            result.append(slate[:])
            # slate.pop()

    # internal node
    if node.left is not None:
        # slate.append(node.val)
        dfs(node.left, target-node.val, result, slate)
        # slate.pop()
    
    if node.right is not None:
        # slate.append(node.val)
        dfs(node.right, target-node.val, result, slate)
        # slate.pop()
    
    # remove the info for the parent
    slate.pop()


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # handle null tree
        if not root:
            return []    

        result = []
        slate = []

        dfs(root, targetSum, result, slate)
        return result