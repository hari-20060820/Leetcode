from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = [[] for _ in range(n)]

        # Build graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS
        q = deque()
        q.append(source)

        visited = [False] * n
        visited[source] = True

        while q:

            node = q.popleft()

            if node == destination:
                return True

            for neighbor in graph[node]:

                if not visited[neighbor]:

                    visited[neighbor] = True
                    q.append(neighbor)

        return False