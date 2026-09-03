class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original=image[sr][sc]
        if image[sr][sc] == color:
            return image
        m=len(image)
        n=len(image[0])
        def dfs(r,c):
            
            if r < 0 or r>=m or c<0 or c>=n:
                return
            if original != image[r][c]:
                return 
            image[r][c]=color
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r,c+1)
        dfs(sr,sc)
        return image