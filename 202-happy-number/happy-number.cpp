class Solution {
public:
    int next(int n)
    {
    int sum=0;
    int re=1;
    
    while(n!=0)
    {
    re=n%10;
    sum=sum+re*re;
    n=n/10;
    }
    return sum;
    }

    bool isHappy(int n) {
       int sum=n;
       unordered_set <int> seen;
       while (sum!=1)
       {
       if(seen.count(sum))
       {
       return false;
       }
       seen.insert(sum);
       sum=next(sum);
        }
        return true;
        }
    
};