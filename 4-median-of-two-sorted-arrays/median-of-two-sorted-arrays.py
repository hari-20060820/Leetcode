class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        data=nums1+nums2
        data=sorted(data)
        n1=len(data)
        if(n1%2==1):
            mid=n1//2
            return data[mid]
        else:
            mid=n1//2
            mid1=n1//2-1
            m=(data[mid]+data[mid1])/2
            return m