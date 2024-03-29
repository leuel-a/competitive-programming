#include <iostream>
#include <vector>
#include <ctype.h>

using std::vector, std::printf;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = k % nums.size();
        reverse(nums, 0, nums.size() - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.size() - 1);
    }
    void reverse(vector <int>&nums, int begin, int end) {
        int temp;
        while (begin < end)
        {
            temp = nums[begin];
            nums[begin] = nums[end];
            nums[end] = temp;
            begin++, end--;
        }
    }
};
