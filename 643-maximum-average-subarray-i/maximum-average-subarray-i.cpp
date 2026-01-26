class Solution {
public:
    /*double findMaxAverage(vector<int>& nums, int k) {

        double av=INT_MIN;
        double av1=INT_MIN;
        if(nums.size()==1)
        return nums[0];

        for(int i=0;i<=nums.size()-k;i++)
        {
        int l=i;
        int r=i+k;
        av=0;
        while(l<r)
        {
            av+=nums[l];
            l++;
            }
        av/=k;
        if(av>av1)
        {
        av1=av;
        }
        }
        cout<<av;
        cout<<av1;
        return av1;
    }*/

    double findMaxAverage(vector<int>& nums, int k) {

        double c_sum = 0;
        for (int i = 0; i < k; i++) {
            c_sum += nums[i];
        }
        double m_sum = c_sum;
        for (int i = k; i < nums.size(); i++) {
            c_sum += nums[i] - nums[i - k];

            if (c_sum > m_sum) {
                m_sum = c_sum;
            }
        }
        return m_sum / k;
    }
};