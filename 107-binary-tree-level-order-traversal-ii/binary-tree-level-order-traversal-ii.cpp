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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        queue<TreeNode*> q;
        if(root==nullptr){
            return res;
        }
        q.push(root);
        while(!q.empty()){
            vector<int> l;
            int size=q.size();
            for(int i =0;i<size;i++){
                TreeNode* r=q.front();
                q.pop();
                l.push_back(r->val);
                if(r->left){
                    q.push(r->left);
                }
                if(r->right){
                    q.push(r->right);
                }
                
            }res.push_back(l);
        }
        reverse(res.begin(),res.end());
        return res;
    }
};