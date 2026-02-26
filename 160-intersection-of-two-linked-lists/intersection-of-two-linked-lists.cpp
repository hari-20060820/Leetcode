/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* A=headA;
        ListNode* B=headB;
        while(A!=nullptr)
        {
            B=headB;
            while(B!=nullptr)
            {
                if(A==B)
                {
                    return A;
                }
                B=B->next;
            }
            A=A->next;
        }
        return nullptr;
    }
};