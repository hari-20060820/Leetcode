class Solution {
public:
    string res;
    bool isPalindrome(string s) {
        for( char c :s)
        {
            if(isalnum(c))
            {
                res+=tolower(c);
            }
        }
        cout<<res;
    
        int n=res.size();
        int i=0,j=n-1;
        while(i<j)
        {
            if(res[i]!=res[j])
            {
                return false;
            }   
            i++;
            j--;
        }
        return true;
    }
};