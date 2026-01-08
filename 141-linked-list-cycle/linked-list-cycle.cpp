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
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> resu;
        ListNode *p=head;
        if( head==NULL)
        {
        return false;
        }
        ListNode *p1=head->next;
        while(p->next != NULL)
        {
            if(resu.find(p)!=resu.end())
            {
            return true;
            }
            resu.insert(p);
            p=p1;
            p1=p1->next;
        }
        return false;
    }
};