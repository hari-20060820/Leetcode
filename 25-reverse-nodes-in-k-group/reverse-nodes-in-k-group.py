# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        node=[]
        curr=head
        while curr:
            node.append(curr)
            curr=curr.next
        n=len(node)
        for i in range(0,n,k):
            if i+k<=n:
                node[i:i+k]=node[i:i+k][::-1]
        for i in range(n-1):
            node[i].next=node[i+1]
        
        if n>0:
            node[-1].next=None
            return node[0]
        return None
        """nstead of reversing pointers immediately,

Store every node in an array.
Reverse every k elements in the array.
Reconnect the nodes.

This is much easier to visualize"""