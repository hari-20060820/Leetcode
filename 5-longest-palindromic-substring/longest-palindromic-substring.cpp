class Solution {
public:
    string longestPalindrome(string s) {
        int start=0;
        int m=0;
        int n=s.size();
        for(int c=0;c<n;c++)
        {
            int l=c;
            int r=c;
            while(l>=0&&r<n&&s[l]==s[r])
            {
                if(r-l+1>m)
                {
                    start=l;
                    m=r-l+1;
                }
                l--;
                r++;
            }

            l=c;
            r=c+1;
             while(l>=0&&r<n&&s[l]==s[r])
            {
                if(r-l+1>m)
                {
                    start=l;
                    m=r-l+1;
                }
                l--;
                r++;
            }
            

        }   
        return s.substr(start,m);     
    }
};