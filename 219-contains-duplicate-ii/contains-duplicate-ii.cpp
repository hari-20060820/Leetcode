#include<unordered_map>
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int n=nums.size();
        unordered_map<int,int> w;
        for( int i=0;i<n;i++)
        {
            if(w.find(nums[i])!= w.end() && (i-w[nums[i]])<=k) return true;

            w[nums[i]]=i;
           
        }

        return false;
}};