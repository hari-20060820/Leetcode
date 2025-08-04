#include<unordered_map>
class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int l=0;
        int n=fruits.size();
        unordered_map<int, int> basket;
        
        int total=0;
        for(int r=0;r<n;r++)
        {
            basket[fruits[r]]++;
            while(basket.size()>2)
            {
                basket[fruits[l]]--;
                if(basket[fruits[l]]==0)
                {
                    basket.erase(fruits[l]);
                }l++;
                
            }total=max(total,r-l+1);

            
        }return total;
    }

};