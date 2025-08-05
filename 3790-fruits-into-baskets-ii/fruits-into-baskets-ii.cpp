class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int count=0;
        int bb=0;
        int basketfix=0;
        int n=fruits.size();
        if(n==1)
        {
            if(fruits[0]<=baskets[0])
            {
                basketfix++;
                fruits.erase(fruits.begin());
                baskets.erase(baskets.begin());
                n--;
                
            }
        }
        else{
        while(count<fruits.size())
        {
            bb=0;
            while(bb<baskets.size())
            {
            if(fruits[count]<=baskets[bb])
            {
                basketfix++;
                fruits.erase(fruits.begin()+count);
                baskets.erase(baskets.begin()+bb);
            
                bb--;
                count--;
                break;
            }
            bb++;}
            count++;
        }
        
    }
return fruits.size();}
};