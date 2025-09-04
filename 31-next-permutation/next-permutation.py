class Solution(object):
    def reversee(self,nums,st,en):
        while(st<en):
            nums[st],nums[en]=nums[en],nums[st]
            st+=1
            en-=1
        

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-2
        while(i>=0 and nums[i]>=nums[i+1]):
            i-=1
        j=len(nums)-1
        if(i>=0):
            while(j>=0 and nums[j]<=nums[i]):
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
         
        self.reversee(nums,i+1,len(nums)-1)
        return nums