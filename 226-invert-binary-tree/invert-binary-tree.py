# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        queue=deque([root])
        while queue:
            node=queue.popleft()
            node.left,node.right=node.right,node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
        """Put the root in the queue.
While the queue is not empty:
Pop a node.
Swap its left and right children.
Push the left child (if it exists).
Push the right child (if it exists).
Return the root."""