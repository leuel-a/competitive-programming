#include <iostream>
#include <vector>
#include <ctype.h>
#include <algorithm>

using std::vector, std::printf, std::max;

class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int i, j, maxLength, zeros;

        maxLength = 0, zeros = 0, i = 0, j = 0;
        while (j < (int)nums.size())
        {
            if (nums[j] == 0)
                zeros++;
            while (zeros > k)
            {
                if (nums[i] == 0)
                    zeros--;
                i++;
            }
            maxLength = max(maxLength, j - i + 1);
            j++;
        }
        return maxLength;
    }
};

