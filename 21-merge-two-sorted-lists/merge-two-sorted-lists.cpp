/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode*  res=new ListNode();
        ListNode* p=list1;
        ListNode* p1=list2;
        ListNode* head=res;
     while(p!=nullptr && p1!=nullptr)
     {
        if(p->val < p1->val)
        {   
            res->next=p;p=p->next;
        }
        else{
           res->next=p1;p1=p1->next;
        }
        
        
        
        res=res->next;
     }
     if(p!=nullptr)
     {
        res->next=p;
     }
      if(p1!=nullptr)
     {
        res->next=p1;
     }

        return head->next;
    }
};