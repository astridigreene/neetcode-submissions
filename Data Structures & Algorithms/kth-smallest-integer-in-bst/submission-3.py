# Definition for a binary tree node.
# class TreeNode:
from types import resolve_bases
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = root.val

        def findSmallest(node):
            nonlocal count, res
            if not node:
                return
            findSmallest(node.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                res = node.val
                return
            findSmallest(node.right)
        findSmallest(root)
        return res
                


