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
        res=[]
        size=len(lists)
        for i in range(size):
            node =lists[i]  
            while node !=None:
                res.append(node.val)
                node=node.next
        res.sort(reverse=True)
        node=None
        head=None
        for i in res:
            node=ListNode(i)
            node.next=head
            head=node
        return head