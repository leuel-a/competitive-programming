/**
 * sortColors - this function will sort an array of numbers based on the description below
 * @nums: the array to be sorted
 * @numsSize: the size of the array to be sorted
 *
 * Description: Given an array nums with n objects colored red, white, or blue, sort them in-place 
 * 	so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
 *
 * 	We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
 *
 * 	-->You must solve this problem without using the library's sort function.
 *
 * Return: Nothing
 */
void sortColors(int* nums, int numsSize){
    
    int i, j, jMin, temp;
    
    for (i = 0; i < numsSize; i++)
    {
        jMin = i;
        for (j = i + 1; j < numsSize; j++)
        {
            if (nums[j] < nums[jMin])
                jMin = j;
        }
        if (jMin != i)
        {
            temp = nums[jMin];
            nums[jMin] = nums[i];
            nums[i] = temp;
        }
    }
}
