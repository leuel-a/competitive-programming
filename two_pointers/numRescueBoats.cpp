#include <iostream>
#include <ctype.h>
#include <algorithm>
#include <vector>

using std::vector, std::sort;


class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int i, j, count;

        sort(people.begin(), people.end());
        i = 0, j = people.size() - 1, count = 0;
        while (i <= j)
        {
            count++;
            if (people[i] + people[j] <= limit)
                i++;
            j--;
        }
        return count;
    }
};
