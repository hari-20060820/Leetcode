class Solution {
public:
    int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
       int l=0;
       int t=0;
       int ma=0;
       int n=fruits.size();
       for(int r=0;r<n;++r)
       {
        t+=fruits[r][1];
        while(l<=r&&min(abs(startPos-fruits[l][0])+(fruits[r][0]-fruits[l][0]),
                        abs(startPos-fruits[r][0])+(fruits[r][0]-fruits[l][0]))>k)
                        {
                            t-=fruits[l][1];
                            ++l;
                        }
                        ma=max(ma,t);
       }
       return ma; 
    }
};