#include <iostream>
#include <ctype.h>
#include <vector>
#include <algorithm>

using std::vector, std::printf;

class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int maxScore = 0, currSum;

        for (int i = 0; i < k; i++)
            maxScore += cardPoints[i];

        currSum = maxScore;
        for (int j = k - 1; j >= 0; j--)
        {
            currSum -= cardPoints[j];
            currSum += cardPoints[cardPoints.size() - k + j];

            maxScore = std::max(maxScore, currSum);
        }
        return maxScore;
    }
};
