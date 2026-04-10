class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> res;
        res.push_back(nums[0]);
        for (int i=1;i<n;i++)
        {
            res.push_back(nums[i+n-1]);
            res.push_back(nums[i]);
        }
        res.push_back(nums[nums.size()-1]);
        return res;
    }
};