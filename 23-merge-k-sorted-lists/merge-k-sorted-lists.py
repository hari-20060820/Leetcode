# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        def mergetwolist(list1,list2):
            dummy=ListNode(0)
            tail=dummy
            while list1 and list2:
                if list1.val>list2.val:
                    tail.next=list2
                    list2=list2.next
                else:
                    tail.next=list1
                    list1=list1.next
                tail=tail.next
            if list1:
                tail.next=list1
            if list2:
                tail.next=list2
            return dummy.next
        n=len(lists)
        if n==0:
            return
        ans=lists[0]
        for i in range(1,n):
            ans=mergetwolist(ans,lists[i])
        return ans