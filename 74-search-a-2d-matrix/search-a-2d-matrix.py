class Solution:
    def binary(self,matrix,n,left,right,target):
        if left>right:
            return False
        mid=left+(right-left)//2
        row=mid//n
        col=mid%n
        val=matrix[row][col]
        if(val == target):
            return True
        elif val < target:
            return self.binary(matrix,n,mid+1,right,target)
        else:
            return self.binary(matrix,n,left,mid-1,target)
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        return self.binary(matrix,n,0,m*n-1 ,target)