class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board=[["." for _ in range(n)] for _ in range(n)]
        res=[]
        def isSafe(row,col):
            r=row-1
            c=col-1
            while r>=0 and c>=0:
                if board[r][c]=="Q":
                    return False
                r=r-1
                c=c-1
            r=row-1
            while r>=0:
                if board[r][col]=="Q":
                    return False
                r=r-1
            r=row-1
            c=col+1
            while r>=0 and c<n:
                if board[r][c]=="Q":
                    return False
                r=r-1
                c=c+1
            return True
        def backtrack(row):
            if row==n:
                res.append(["".join(r) for r in board]) 
                return 
            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"

                    backtrack(row + 1)

                    board[row][col] = "."
        backtrack(0)
        return res