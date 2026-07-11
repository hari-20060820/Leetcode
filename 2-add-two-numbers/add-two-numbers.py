# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s=0
        place=1
        while (l1):
           s=s+l1.val*place
           place*=10
           l1=l1.next
        s1=0
        place=1
        while (l2):
           s1=s1+l2.val*place
           place*=10
           l2=l2.next
        s3=s1+s
        head=None
        t=None
        if s3==0:
            return ListNode(0)
        while (s3):
            r=s3%10
            s3=s3//10
            newNode=ListNode(r)
            if not head:
                head=newNode
                t=head
                continue
            t.next=newNode
            t=newNode
        return head