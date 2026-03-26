class Solution {
public:
    int climb (int n,int dp[])
    {
        if(n==1) return 1;
        if(n==2) return 2;
        if(dp[n]!= -1) return dp[n];
        
        dp[n]=climb(n-1,dp)+climb(n-2,dp);
        return dp[n];
    }

    int climbStairs(int n) {
        int dp[100];
        for(int i=0;i<=n;i++)
        {
            dp[i]=-1;
        }
        return climb(n,dp);
    }
};