class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row=len(matrix)
        col=len(matrix[0])
        left=0
        right=col-1
        top=0
        bottom=row-1
        res=[]
        while left <= right and top <= bottom:
            for t in range(left,right+1):
                res.append(matrix[top][t])

            top+=1
            for tb in range(top,bottom+1):
                res.append(matrix[tb][right])
            right-=1
            if top<= bottom:
                for lr in range(right,left-1,-1):
                    res.append(matrix[bottom][lr])
                bottom-=1
            if left<=right:
                for bt in range(bottom,top-1,-1):
                    res.append(matrix[bt][left])
                left+=1
        return res