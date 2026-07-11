# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root :
            return []
        
        res=[]
        queue=deque([root])
        while queue :
            size=len(queue)
            levels=[]
            for _ in range(size):
                t=queue.popleft()
                levels.append(t.val)
                if t.left:
                    queue.append(t.left)
                if t.right:
                    queue.append(t.right)
            res.append(levels)
        return res