class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary (left,right,target):
            if left>right:
                return -1 
            else:
                mid=left + (right-left)//2
                if nums[mid] == target:
                    return mid 
                elif nums[mid]<target:
                    return binary(mid+1,right,target)
                elif nums[mid]>target:
                    return binary(left,mid-1,target)
        a=binary(0,len(nums)-1,target)
        return a