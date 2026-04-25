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
    int bfs(TreeNode* root, int c, int target){
        queue<pair<TreeNode*,int>> q;
        if(root==nullptr)
        return 0;
        q.push({root,root->val});
        while(!q.empty()){
            auto front = q.front();
            q.pop();
            TreeNode* r=front.first;
            int currsum=front.second;
            if(r->left == nullptr && r->right== nullptr){
            if(currsum==target){
                return 1;
            }
            }

            if(r->left){
                q.push({r->left,currsum+r->left->val});
            }
            if(r->right){
                q.push({r->right,currsum+r->right->val});
            }

        }
        return 0;
    }
    bool hasPathSum(TreeNode* root, int targetSum) {
        if(bfs(root,0,targetSum)==1){
            return true;
        }
        else{
            return false;
        }
    }
};