# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast= head
        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next
        
        mid=slow.next
        slow.next=None
        curr=mid
        p=None
        n=None
        while curr:
            n=curr.next
            curr.next=p
            p=curr
            curr=n
        first=head
        second=p
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1

            first=temp1
            second=temp2
        


            