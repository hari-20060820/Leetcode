class Solution {
public:
    vector<vector<int>> res;
    void backtrack(int index,vector<int> can, int target,int sum,vector<int>& temp)
    {
        if(sum==target){
            res.push_back(temp);
            return;
        }
    
        for (int i=index;i<can.size();i++)
        {
            if (i > index && can[i] == can[i - 1]) continue;
             if(sum+can[i]>target){
            break;
        }
            temp.push_back(can[i]);
            backtrack(i+1,can,target,sum+can[i],temp);
            temp.pop_back();
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> temp;
        sort(candidates.begin(), candidates.end());
        backtrack(0,candidates,target,0,temp);
        return res;
    }
};