#include <iostream>
#include <ctype.h>
#include <vector>

using std::vector, std::printf;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int i, last, leftSum;
        vector<int> prefixSum(nums.size());

        prefixSum[0] = nums[0];
        for (i = 1; i < (int)nums.size(); i++)
            prefixSum[i] = nums[i] + prefixSum[i - 1];

        last = (int)nums.size() - 1, leftSum = 0;
        for (i = 0; i < (int)nums.size(); i++)
        {
            if (prefixSum[last] - prefixSum[i] == leftSum)
                return i;
            leftSum = prefixSum[i];
        }
        return -1;
    }
};
