from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        queue=deque()
        if not board or not board[0]:
            return 
        row =len(board)
        col=len(board[0])

        for i in range(row):
            if board[i][0]=="O":
                queue.append((i,0))
            if board[i][col-1]=="O":
                queue.append((i,col-1))
        for j in range(col):
            if board[0][j]=="O":
                queue.append((0,j))
            if board[row-1][j]=="O":
                queue.append((row-1,j))
        while queue:
            size=len(queue)
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            
            r,c=queue.popleft()
            if board[r][c]!="O":
                continue
                
            board[r][c]="T"
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if (0<=nr<row and 0<=nc<col and board[nr][nc]=="O"):
                    queue.append((nr,nc))

        for i in range(row):
            for j in range(col):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="T":
                    board[i][j]="O"
                