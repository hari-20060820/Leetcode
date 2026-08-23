class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        s=list(s)
        s=sorted(s)
        for i in range(len(s)):
            nums[i]=s[i]
        return len(s)