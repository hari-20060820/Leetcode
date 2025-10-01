class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int m=0;
        int minp=INT_MAX;
        for(int pr : prices)
        {
            if(pr<minp){
            minp=pr;}

            if(pr-minp>m)
            {
                m=pr-minp;
            }
        }
        return m;
    }
};