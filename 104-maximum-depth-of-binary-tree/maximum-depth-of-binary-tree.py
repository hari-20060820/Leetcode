# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res=[]
        if not root:
            return 0
        def dfs(level,node):
            if not node.left and not node.right :
                res.append(level)
            if node.left:
                dfs(level+1,node.left)
            if node.right:
                 dfs(level+1,node.right)
        dfs(0,root)
        return max(res)+1
