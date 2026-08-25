class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum=nums[0]
        best_sum=nums[0]
        for i in range(1,len(nums)):
            curr_sum=max(nums[i],curr_sum+nums[i])
            best_sum=max(best_sum,curr_sum)
        return best_sum