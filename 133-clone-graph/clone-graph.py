"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node :
            return None
        copies={}
        copies[node]=Node(node.val)
        queue=deque([node])
        while queue:
            current=queue.popleft()
            for neighbors in current.neighbors:
                if neighbors not in copies:
                    copies[neighbors]=Node(neighbors.val)
                    queue.append(neighbors)
                copies[current].neighbors.append(copies[neighbors])
        return copies[node]