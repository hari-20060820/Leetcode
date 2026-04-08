class Solution {
public:
vector<vector<int>> res;
void backtrack(vector<int> nums,int s,vector<int>& temp,vector<bool>& used)
{
    if(temp.size()==s){
        res.push_back(temp);
        return;
    }
    for(int i=0;i<nums.size();i++){
        if(used[i]) continue;
        used[i]=true;
        temp.push_back(nums[i]);
        backtrack(nums,s,temp,used);
        temp.pop_back();
        used[i]=false;
    }
}
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> temp;
        vector<bool> used(nums.size(),false);
        backtrack(nums,nums.size(),temp,used);
        return res;
    }
};