#include <vector>
#include <iostream>
#include <ctype.h>

using std::vector;

/**
 * moveZeroes - moves all zeros of a vector to the end,
 * while maintaining the relative order of the non-zero
 * elements
 * @nums: the vector to be reordered
 *
 * Return: Always nothing.
*/
void moveZeroes(vector<int>& nums) {
    std::size_t count = 0;
    int i;

    for (i = 0; i < (int)nums.size();i++)
        if (nums[i] != 0)
            nums[count++] = nums[i];

    while (count < nums.size())
        nums[count++] = 0;
}
