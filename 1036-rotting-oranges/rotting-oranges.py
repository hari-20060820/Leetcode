class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        col=len(grid[0])
        queue=deque()
        fresh=0
        minute=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh == 0:
            return 0
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        while queue and fresh>0:
            size=len(queue)
            
            for _ in range(size):
                r,c=queue.popleft()
                for nr,nc in directions:
                    dr=r+nr
                    dc=c+nc
                    if (0<=dr<row and 0<=dc<col and grid[dr][dc]==1):
                        grid[dr][dc]=2
                        queue.append((dr,dc))
                        fresh-=1
            minute+=1
        if fresh>0:
            return -1 
        return minute     
