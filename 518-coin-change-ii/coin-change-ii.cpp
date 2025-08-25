class Solution {
public:
    int var=0;
    int op=0;
    int func(int a,vector<int>& c,int i,vector<vector<int>>& m)
    {
    if(a==0)return 1;
    if(a<0||i==c.size())return 0;
    if(m[i][a]!=-1) return m[i][a];
    int include=func(a-c[i],c,i,m);
    int exclude=func(a,c,i+1,m);
    return m[i][a]=include+exclude;
    }
    
    int change(int amount, vector<int>& coins) {
        vector<vector<int>> m(coins.size(),vector<int>(amount+1,-1));
        op=func(amount,coins,0,m);

        return op;
    }
};