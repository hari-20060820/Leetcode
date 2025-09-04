class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> hashset;
        vector<int> ar;
        int j=0;
        int n=nums.size();
        for(int i=0;i<n;i++)
        {
            int sum =target-nums[i];
            if(hashset.count(sum))
            {
                return {hashset[sum],i};
            }
            hashset[nums[i]]=i;
        }
        return {};
    }
};