#include <vector>
#include <iostream>

using std::vector, std::printf;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prefixProduct, suffixProduct;
        vector<int> result(nums.size(), 1);

        prefixProduct = suffixProduct = 1;
        for (int i = 0, n = nums.size() - 1; i < (int)nums.size(); i++)
        {
            result[i] *= prefixProduct, prefixProduct *= nums[i];
            result[n - i] *= suffixProduct, suffixProduct *= nums[n - i];
        }
        return result;
    }
};
