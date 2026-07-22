class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        leftmax=[0]*n
        rightmax=[0]*n
        leftmax[0]=height[0]
        rightmax[n-1]=height[n-1]
        for i in range(len(height)):
            leftmax[i]=max(leftmax[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i])
        water=0
        for i in range(n):
            water+=min(leftmax[i],rightmax[i])-height[i]
        return water