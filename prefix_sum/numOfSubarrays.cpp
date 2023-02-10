#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int i = 0 , sum = 0 ,count = 0;
        unordered_map<int,int> map;
        while(i < nums.size())
        {
            if (nums[i] % 2 != 0)
                sum+=1;
            if (sum == k)
                count++;
            if (map.find(sum-k) != map.end())
                count += map[sum-k];

            map[sum]++;
            i++;
        }
        return count;
    }
};
