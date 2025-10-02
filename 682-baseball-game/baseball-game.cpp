#include<cctype>

class Solution {
public:
    vector<int> arr;
    int index=0;
    void x(int a)
    {
        arr.push_back(a);
        
    }
    void d()
    {
        arr.push_back(arr.back()*2);
        
    }
    void r()
    {
        arr.pop_back();
        
    }

    void p()
    {
        arr.push_back(arr[arr.size()-1]+arr[arr.size()-2]);
    }
    int calPoints(vector<string>& operations) {
        for( int i=0; i<operations.size();i++)
        {
            if(operations[i]=="+")
            {
                p();
            }
            else if(operations[i]=="C")
            {
                r();
            }
            else if(operations[i]=="D")
            {
                d();
            }
            else
            {
                int val=stoi(operations[i]);
                x(val);
            }
        }
        int res=0;
        for(int b: arr)
        {
            res+=b;
        }
        return res;
    }
};