# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' if not head:
            return head
        p=head
        p1=head.next
        while p1:
            if p.val>p1.val:
                p2=head
                while p2 != p1:
                    if p2.val>p1.val:
                        p2.val,p1.val=p1.val,p2.val
                    p2=p2.next
            p=p.next
            p1=p1.next
        return head'''
        res = []
        while head:
            res.append(head.val)
            head = head.next
        
        res.sort()
        dummy = ListNode()
        curr = dummy
        for num in res:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next