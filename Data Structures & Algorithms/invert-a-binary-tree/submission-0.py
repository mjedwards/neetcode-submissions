# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        queue = deque()
        queue.append(root)

        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)
        
        return root
