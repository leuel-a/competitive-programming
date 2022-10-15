/**
 * smallerNumbersThanCurrent - this function will find how many numbers are
 * 	smaller than the numbers in the array
 *
 * @nums: the array of numbers to be checked
 * @numsSize: size of the nums array
 * @returnSize: size of the return array
 *
 * Description:
 * 	Given the array nums, for each nums[i] find out how many numbers in 
 * 	the array are smaller than it. That is, for each nums[i] you have to 
 * 	count the number of valid j's such that j != i and nums[j] < nums[i].
 *
 * Return: The new array with the correct amount of elements less than the elements
 */


int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize){
    
    int *countLess, count, i, j;
    
    *returnSize = numsSize;    
    countLess = malloc(sizeof(int) * (*returnSize));
    for (i = 0; i < numsSize; i++)
    {
        for (j = 0; j < numsSize; j++)
        {
            if (j!= i && nums[j] < nums[i])
                count++;
        }
        countLess[i] = count;
        count = 0;
    }
    return countLess;

}
