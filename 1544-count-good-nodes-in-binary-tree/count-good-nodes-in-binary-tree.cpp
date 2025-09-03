/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int count=0;
    void nodetraverseleft(TreeNode* root,int m )
    {
        if(root==nullptr)
        {
            return;
        }
        if(m <= root->val)
        {
            m=root->val;
            count++;
        }
        nodetraverseleft(root->left,m);
        nodetraverseleft(root->right,m);
    }
    int goodNodes(TreeNode* root) {
        
        nodetraverseleft(root,root->val);
        return count;
    }
};