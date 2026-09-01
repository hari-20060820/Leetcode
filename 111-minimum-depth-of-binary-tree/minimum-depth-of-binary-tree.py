# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def solve(root):
            if not root:
                return 0
            if not root.right and not root.left:
                return 1
            if not root.left:
                return solve(root.right) + 1
            if not root.right :
                return solve(root.left) + 1
            return min(solve(root.left),solve(root.right))+1
        return solve(root)