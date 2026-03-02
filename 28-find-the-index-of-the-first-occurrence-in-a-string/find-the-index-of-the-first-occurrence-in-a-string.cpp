class Solution {
public:
    int strStr(string haystack, string needle) {
        int l=0;
        int n=haystack.length();
        int n1=needle.length();
        if(n1 == 0) return 0;  
        if(n<n1)
        {
            return -1;
        }
        for(int i=0;i<=n-n1;i++)
        {bool f=true;
            for(int j=0;j<n1;j++)
            {
                if(haystack[i+j]!=needle[j])
                {
                    f=false;
                    break;
                }
               
            } if(f){
                    return i;
                }
        }
        return -1;
    }
};