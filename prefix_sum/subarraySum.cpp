#include <iostream>
#include <ctype.h>
#include <vector>
#include <unordered_map>

using std::vector, std::printf;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k)
    {
        std::unordered_map<int, int> hash;
        int count = 0, sum = 0, i;

        for (i = 0; i < (int)nums.size(); i++)
        {
            sum += nums[i];
            if (sum == k)
                count++;

            if (hash.find(sum - k) != hash.end())
                count += hash[sum - k];
            hash[sum]++;
        }
        return count;
    }
};
