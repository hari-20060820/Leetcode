class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int,int> a;
        int res=0;
        for(int i=0;i<nums.size();i++)
        {
        a[nums[i]]++;
       
        } 
        for(int i=0;i<nums.size();i++)
        {if(a[nums[i]]==1)
        {
        res=nums[i];
        }}
    return res;

    }
};