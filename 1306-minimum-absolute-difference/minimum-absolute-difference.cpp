#include <cmath>
class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        vector<vector<int>> res;
        sort(arr.begin(), arr.end());
        int l = 0;
        int r = l + 1;
        int sub = abs(arr[r] - arr[l]);
        l++;
        r++;
        while (r < arr.size()) {
            int sub1 = abs(arr[r] - arr[l]);
            if (sub1< sub) {
                sub=sub1;
            }
            l++;
            r++;
        }
        l = 0;
        r = l + 1;
        while (r < arr.size()) {
            int sub1 = abs(arr[r] - arr[l]);
            if (sub1== sub) {
                    res.push_back(vector<int>{arr[l],arr[r]});
            }
            l++;
            r++;
        }
        return res;
    }
};