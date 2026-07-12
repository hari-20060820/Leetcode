class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        queue=deque()
        row=len(grid)
        col=len(grid[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        count=0
        visited=set()
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1" and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
                    count+=1

                while queue:
                    r,c=queue.popleft()
                    for dr,dc in directions:
                        nr=r+dr
                        nc=c+dc
                        if (0<=nr<row) and (0<=nc<col) and grid[nr][nc]=="1" and (nr,nc) not in visited:
                            visited.add((nr,nc))
                            queue.append((nr,nc))
        
        return count 
        """Traverse every cell.
If you find an unvisited land ('1'):
Increment island count.
Start BFS from this cell.
Mark every connected land as visited.
Continue scanning.
Return the count."""