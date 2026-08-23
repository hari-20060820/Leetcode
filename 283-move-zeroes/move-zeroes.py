class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        if len(nums) == 1:
            return nums 
        for r in range(len(nums)):
            if nums[r]!=0:
                s=nums[r]
                
                
                nums[r]=0
                nums[l]=s
                l+=1
        return nums
        