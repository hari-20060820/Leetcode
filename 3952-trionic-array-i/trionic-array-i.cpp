class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int n=nums.size();
        int i=1;
        int p=0;
        while(i<n && nums[i-1]<nums[i]  )
        {
           
            i++;
        }
        p=i-1;
        int q=p;
        while(i<n && nums[i-1]>nums[i] )
        {
            
            i++;
        }
        q=i-1;
        int flag=q;
        while(  i<n && nums[i-1]<nums[i])
        {
            i++;
        }
        flag=i-1;
        return (p!=q) && (q!=flag) && (flag==n-1) && (p!=0);
    }
};