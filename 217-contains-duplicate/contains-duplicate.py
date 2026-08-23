class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
            if freq.get(nums[i]) >1:
                return True
        return False