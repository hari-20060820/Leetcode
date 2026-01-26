class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int l=0;
        int r=k-1;
        int min=nums[r]-nums[l];
        r++;
        l++;
        while(r<nums.size())
        {
            int min1=nums[r]-nums[l];
            if(min1<min)
            {
            min=min1;
            }
            l++;
            r++;
            }
            return min;
    }
};