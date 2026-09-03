from collections import deque

class Solution:
    def maxDepth(self, root):

        if root is None:
            return 0

        q = deque()
        q.append(root)

        depth = 0

        while q:

            level_size = len(q)

            for _ in range(level_size):

                node = q.popleft()

                for child in node.children:
                    q.append(child)

            depth += 1

        return depth