"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
def bfs(node):
    q = deque()
    q.append(node)

    while q:
        prevnode = None
        for _ in range(len(q)):
            node = q.popleft()
            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)
    
            if prevnode is not None:
                prevnode.next = node

            prevnode = node
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        bfs(root)

        return root
        