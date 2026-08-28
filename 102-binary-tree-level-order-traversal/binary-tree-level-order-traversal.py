# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([root])
        levels=[]
        if not root:
            return []
        while q:
            s=len(q)
            l=[]
            for _ in range(s):
                node=q.popleft()
                l.append(node.val)
                if node.left :
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels.append(l)
        return levels