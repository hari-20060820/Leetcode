class Solution:
    def binary(self,nums,left,right,target):
        if left>right:
            return -1
        mid=left+(right-left)//2
        if (nums[mid]==target):
            return mid
        elif (nums[mid] < target):
            return self.binary(nums,mid+1,right,target)
        else:
            return self.binary(nums,left,mid-1,target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary(nums,0,len(nums)-1,target)