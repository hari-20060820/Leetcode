class Solution {
public:

    int binary(vector<int> nums,int target,bool bias)
    {
        int n = nums.size();
        int l = 0 , r = n-1;
        int mid=(r-l)/2;
        int i=-1;
        while(l<=r)
        {
            mid=l+(r-l)/2;
            if(nums[mid]>target)
            {
                r=mid-1;
            }
            else if ( nums[mid]<target)
            {
                l=mid+1;
            }
            else{
                i=mid;
                if (bias) {
                    r=mid-1;
                }
                else{
                    l=mid+1;
                }
            }
        }
        return i;
    }
    vector<int> searchRange(vector<int>& nums, int target) {
        
        int left= binary(nums,target,true);
        int right= binary(nums,target,false);
        return vector<int>({left,right});
    }
    
};