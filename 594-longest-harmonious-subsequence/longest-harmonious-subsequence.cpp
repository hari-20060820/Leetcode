#include<unordered_map>
class Solution {
public:
    int findLHS(vector<int>& nums) {
        int taken=0;
        unordered_map<int,int> a;
        for(int i:nums)
        {
            a[i]++;
        }
        int l=0;
        for(auto& i: a)
        {
            int num=i.first;
            if(a.find(num+1)!=a.end())
            {
                
                l=max(l,i.second+a[num+1]);
            }
        }
        return l;
    }
};