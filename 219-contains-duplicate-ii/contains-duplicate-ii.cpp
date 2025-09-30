#include<unordered_map>
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int n=nums.size();
        unordered_map<int,int> w;
        for( int i=0;i<n;i++)
        {
            if(w.find(nums[i])!= w.end() && abs(i-w[nums[i]])<=k) return true;

            w[nums[i]]=i;
            if(w.size()>k)
            {
                w.erase(nums[i-k]);
            }
        }

        return false;
}};