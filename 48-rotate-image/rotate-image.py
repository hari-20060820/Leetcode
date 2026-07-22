class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])

        matrix1=[[0]* c for _ in range(r)]
        for i in range(c):
            for j in range(r-1,-1,-1):
                matrix1[i][abs(j-c+1)]=matrix[j][i]
        for i in range(r):
            for j in range(c):
                matrix[i]=matrix1[i]