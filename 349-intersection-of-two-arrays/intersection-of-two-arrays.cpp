class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> a(nums1.begin(),nums1.end());
        unordered_set<int> b(nums2.begin(),nums2.end());
        vector<int> res;
        for(int x :a){
            if(b.find(x)!=b.end())
            {
                res.push_back(x);
                
            }
            
        }
        return res;
    }
};