class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        int n = nums.size();
        if (n == 0) return res; // Handle empty case

        for (int i = 0; i < n; i++) {
            int start = nums[i];

            // Keep moving 'i' forward while the numbers are consecutive
            while (i + 1 < n && nums[i + 1] == nums[i] + 1) {
                i++;
            }

            if (start != nums[i]) {
                // YOUR LOGIC: variable + string + variable
                res.push_back(to_string(start) + "->" + to_string(nums[i]));
            } else {
                // YOUR LOGIC: variable converted to string
                res.push_back(to_string(start));
            }
        }
        return res;
    }
};