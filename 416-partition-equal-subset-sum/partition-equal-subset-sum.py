class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        target=total // 2
        if total %2 != 0:
            return False
        dp=[False]*(target+1)
        dp[0]=True
        for n in nums:
            for s in range(target,n-1,-1):
                dp[s]=dp[s] or dp[s-n]
            if dp[target] :
                return True
        return dp[target] 