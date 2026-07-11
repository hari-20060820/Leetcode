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
        """
        ### **Clone Graph (BFS) - Short Steps**

1. If the graph is empty, return `None`.
2. Create a **dictionary** (`copies`) to map **original node → cloned node**.
3. Clone the starting node and store it in the dictionary.
4. Create a **queue** and push the starting node.
5. While the queue is not empty:

   * Pop a node from the queue.
   * Traverse all its neighbors.
   * If a neighbor is not in the dictionary:

     * Create its clone.
     * Store it in the dictionary.
     * Push the original neighbor into the queue.
   * Connect the cloned current node to the cloned neighbor using the dictionary.
6. Return the clone of the starting node (`copies[node]`).

### **Key Idea**

* **Queue** → Traverses the graph using BFS.
* **Dictionary (`copies`)** → Stores the mapping from **original node → cloned node** and also prevents visiting the same node multiple times.

        """