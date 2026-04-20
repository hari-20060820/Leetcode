class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> has;
        for(int i=0;i<nums.size();i++){
            int sum=target-nums[i];
            if(has.count(sum)){
                return {has[sum],i};
            }
            has[nums[i]]=i;
        }
        return {};
    }
};