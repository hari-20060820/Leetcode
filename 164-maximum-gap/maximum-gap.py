class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        ma=float("-INF")
        for i in range(len(nums)-1):
            gap=nums[i+1]-nums[i]
            if gap > ma:
                ma=gap
        return ma