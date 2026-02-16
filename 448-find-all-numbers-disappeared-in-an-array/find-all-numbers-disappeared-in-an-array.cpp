#include<set>
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        set<int> a(nums.begin(),nums.end());
        vector<int> res;
        for(int i=1;i<=nums.size();i++)
        {
            if(a.find(i)==a.end()) 
            {
                res.push_back(i);
            }
        }
        return res;
    }
};