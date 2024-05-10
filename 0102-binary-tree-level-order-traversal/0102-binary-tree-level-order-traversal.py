# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None

        # Simple BFS code for tree

        q = deque()
        q.append(root)

        ans = []
        cur_level_nodes = []

        while q:
            temp = []

            for i in range(len(q)):
                node = q.popleft()
                
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                temp.append(node.val)
            ans.append(temp)

        return ans
        