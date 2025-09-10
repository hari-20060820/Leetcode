class Solution {
public:
    void merge(vector<int>& nums, int l, int m, int r) {
        int le = m - l + 1;
        int ri = r - m;

        // temporary arrays
        int* ld = new int[le];
        int* rt = new int[ri];

        for (int i = 0; i < le; i++) {
            ld[i] = nums[l + i];
        }
        for (int j = 0; j < ri; j++) {
            rt[j] = nums[m + 1 + j];
        }

        int i = 0, j = 0, k = l;

        // merge the two halves
        while (i < le && j < ri) {
            if (ld[i] <= rt[j]) {
                nums[k] = ld[i];
                i++;
            } else {
                nums[k] = rt[j];
                j++;
            }
            k++;
        }

        // copy leftovers
        while (i < le) {
            nums[k] = ld[i];
            i++;
            k++;
        }

        while (j < ri) {
            nums[k] = rt[j];
            j++;
            k++;
        }

        // free memory
        delete[] ld;
        delete[] rt;
    }

    void mergesort(vector<int>& nums, int l, int r) {
        if (l >= r) return;

        int mid = (l + r) / 2;

        mergesort(nums, l, mid);
        mergesort(nums, mid + 1, r);
        merge(nums, l, mid, r);
    }

    vector<int> sortArray(vector<int>& nums) {
        mergesort(nums, 0, nums.size() - 1);
        return nums;
    }
};
