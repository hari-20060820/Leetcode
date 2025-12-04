class Solution {
public:
    string intToRoman(int num){
        vector<int> ar={1,4,5,9,10,40,50,90,100,400,500,900,1000};
        vector<string> a={"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
        string r="";
        for(int i=ar.size()-1;i>=0;i--)
        {
            while(num>=ar[i])
            {
                num-=ar[i];
                r+=a[i];
            }
        }
        cout<<r;
        return r;
    }
};