class Solution {
public:
    vector<string> res;
    void backtrack(int n,int o,int c,string temp){
        if(temp.size() == 2*n){
            res.push_back(temp);
            return;
        }
        if(o <n){
            backtrack(n,o+1,c,temp+'(');
        }
        if(c<o){
            backtrack(n,o,c+1,temp+')');
        }

    }
    vector<string> generateParenthesis(int n) {
        string t;
        backtrack(n,0,0,t);
        return res;
    }
};