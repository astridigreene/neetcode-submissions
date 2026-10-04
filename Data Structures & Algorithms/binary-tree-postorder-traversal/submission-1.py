# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        last = None

        while stack:
            top = stack[-1]
            if (not top.right and not top.left) or (last and (last == top.right or last == top.left)):
                res.append(top.val)
                last = top
                stack.pop()
            else:
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)

        return res
            


