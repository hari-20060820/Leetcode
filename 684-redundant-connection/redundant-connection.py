from collections import defaultdict,deque
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph=defaultdict(list)
        for u,v in edges:
            if u in graph and v in graph:
                queue=deque([u])
                visited=set([u])

                while queue:
                    node=queue.popleft()
                    if node==v:
                        return [u,v]
                    for nei in graph[node]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            graph[u].append(v)
            graph[v].append(u)
