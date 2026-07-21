class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma={}
        for i in range(len(nums)):
            if nums[i] not in ma:
                ma[nums[i]]=0 
            ma[nums[i]]=ma[nums[i]]+1
        N=len(nums)
        i=0
        while i<N:
            if ma[nums[i]] > 2:
                ma[nums[i]]=ma[nums[i]]-1
                del nums[i]
                N-=1
                i-=1
            i+=1
                
         
        