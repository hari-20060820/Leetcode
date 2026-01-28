class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        g=[[] for _ in range(n)]
        for u,v,w in edges:
            g[u].append((v,w))
            g[v].append((u,w*2))

        dist=[float('inf')]*n
        dist[0]=0
        heap=[(0,0)]
        visited=[False]*n
        while heap:
            d,u=heapq.heappop(heap)
            if (u==n-1): 
                return d
            if visited[u]:
                continue
            visited[u]=True
            for v,w in g[u]:
                if (dist[u]+w <dist[v]):
                    dist[v]=dist[u]+w
                    heapq.heappush(heap,(dist[v],v))
        return -1
        