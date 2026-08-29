# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d=0
        def p(node):    
            nonlocal d
            if not node:
                return 0
            left=p(node.left)
            right=p(node.right)
            d=max(d,left+right)
            return max(left,right)+1

        t=p(root)
        return d