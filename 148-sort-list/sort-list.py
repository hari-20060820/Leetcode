# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,left,right):
        dum=ListNode(0)
        tail=dum
        while left and right:
            if left.val < right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            tail=tail.next
        if (left):
            tail.next=left
            
        if right:
            tail.next=right
            
        return dum.next

    def mergesort(self,head):
        if not head or not head.next:
            return head
        slow=head
        fast=head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        mid= slow.next
        slow.next=None

        left=self.mergesort(head)
        right=self.mergesort(mid)
        return self.merge(left,right)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head=self.mergesort(head)
        return head