class Solution {
    unordered_map<int,int> has;
public:
    int majorityElement(vector<int>& nums) {
        unordered_map <int,int> hash; 
        int n = nums.size();
        for(int i=0;i<n;i++)
        {
            hash[nums[i]]++;
            if(hash[nums[i]]>(n/2))
            return nums[i];
        }
return 0;
    }
};