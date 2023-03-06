#!/usr/bin/python3

class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        minIndex, maxIndex = 0, 0
        for i in range(1, len(nums)):
            if nums[minIndex] > nums[i]:
                minIndex = i
            if nums[maxIndex] < nums[i]:
                maxIndex = i

        minDeletion = max(maxIndex, minIndex) + 1
        count, i, j = 0, 0, len(nums) - 1
        
        minDeletion = min(minDeletion, count)
        return minDeletion



sol = Solution()
sol.minimumDeletions([-14,61,29,-18,59,13,-67,-16,55,-57,7,74])
