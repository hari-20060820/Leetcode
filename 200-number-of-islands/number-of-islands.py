class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        d=[(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count+=1
                    q=deque()
                    q.append((i,j))
                    grid[i][j]='0'
                    while q:
                        nr,nc=q.popleft()
                        for r,c in d:
                            dr=nr+r
                            dc=nc+c
                            if 0<=dr<m and 0<=dc<n and grid[dr][dc]=='1':
                                grid[dr][dc]='0'
                                q.append((dr,dc))
        return count