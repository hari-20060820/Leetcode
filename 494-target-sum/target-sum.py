class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        if abs(target)> total or (total+target)%2 != 0:
            return 0 
        req=abs(target-sum(nums)) // 2
        dp=[0]*(req+1)
        dp[0]=1
        for n in nums:
            for s in range(req,n-1,-1):
                dp[s]+=dp[s-n] 
        return dp[req]