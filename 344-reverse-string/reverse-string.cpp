class Solution {
public:
    void reverseString(vector<char>& s) {
        int n=s.size();
        for(int i=0,j=n-1;i<(n/2),j>(n/2)-1;i++,j--)
        {
            swap(s[i],s[j]);
        }
    }
};