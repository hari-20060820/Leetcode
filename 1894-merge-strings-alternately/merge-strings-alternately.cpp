class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int l=0;
        int r=0;
        string re="";
        while(l<word1.size() && r<word2.size())
        {
            re+=word1[l++];
            re+=word2[r++];
        }
        while(l<word1.size() )
        {
            re+=word1[l++];
            
        }
        while(r<word2.size() )
        {
            re+=word2[r++];
            
        }
    return re;}
};