class Solution {
public:
vector<vector<int>> res;
    void backtrack(vector<int> nums,int s, vector<int>& temp,vector<bool>& used){
        if(temp.size()==s){
            res.push_back(temp);
            return;
        }
        for(int i=0;i<nums.size();i++){
            if(used[i]) continue;
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
            used[i]=true;
            temp.push_back(nums[i]);
            backtrack(nums,s,temp,used);
            temp.pop_back();
            used[i]=false;
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<bool> used(nums.size(),false);
        vector<int> temp;
        sort(nums.begin(),nums.end());
        backtrack(nums,nums.size(),temp,used);
        return res;
    }
};