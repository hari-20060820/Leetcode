class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int m=0;
        int minp=INT_MAX;
        for(int pr : prices)
        {
            
            minp=min(pr,minp);

            m=max(pr-minp,m);
            
        }
        return m;
    }
};