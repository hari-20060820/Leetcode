class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l=0;
        for(int r=1;r<nums.size();r++)
        {
        if(nums[l]<nums[r])
        {
        nums[l+1]=nums[r];
        l++;
        }
       
        }
        return l+1;
    }
};