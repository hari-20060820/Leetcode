class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
       /* unordered_map <string,int> f;
  
        vector<int> res;
        if(words.empty())
        {
        return res;
        }
        int wl=words[0].length();
        int wc=words.size();
        int wn=wl*wc;
        int i=0;
        for(string w:words)
        {
        f[w]++;
        }
        

        for(i =0;i+wn<=s.length();i++)
        {
        unordered_map<string,int> seen;
        int j=0;
        for(j=0;j<wc;j++)
        {
        int start=i+j*wl;
        string sam=s.substr(start,wl);
        if(f.find(sam)==f.end())
        break;
        seen[sam]++;
        if(seen[sam]>f[sam])
        break;
        }
        if(j==wc)
            res.push_back(i);
            }
        return res;*/

        //gpt code --
        

        vector<int> res;
        if (words.empty()) return res;

        int wl = words[0].length();
        int wc = words.size();
        int n  = s.length();

        unordered_map<string,int> freq;
        for (string &w : words)
            freq[w]++;

        // Try all word-length offsets
        for (int offset = 0; offset < wl; offset++) {

            unordered_map<string,int> seen;
            int left = offset, count = 0;

            for (int right = offset; right + wl <= n; right += wl) {

                string word = s.substr(right, wl);

                if (freq.count(word)) {
                    seen[word]++;
                    count++;

                    while (seen[word] > freq[word]) {
                        string leftWord = s.substr(left, wl);
                        seen[leftWord]--;
                        left += wl;
                        count--;
                    }

                    if (count == wc)
                        res.push_back(left);

                } else {
                    seen.clear();
                    count = 0;
                    left = right + wl;
                }
            }
        }

        return res;
    
    }
};