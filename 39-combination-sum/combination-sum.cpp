class Solution {
public:
    vector<vector<int>> res;
    
    void backtrack(int index,vector<int>& can,int target,int sum,vector<int>& temp){
        if(sum==target){
                res.push_back(temp);
                return;
            }

            if(sum>target)
            {
                return;
            }

        for (int i=index;i<can.size();i++){
            temp.push_back(can[i]);
            backtrack(i,can,target,sum+can[i],temp);
            temp.pop_back();
            
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> temp;
        backtrack(0,candidates,target,0,temp);
        return res;
    }
};