
/**
 * countSwaps - this function will count the number of swaps needed
 * to sort an array(descending order) to ascending order
 *
 * Description: this function implements the Bubble Sort Algorithm
 *
 * @a_count: the size of the array
 * @a: the array to be sorted
 *
 * Return: Nothing
 */
void countSwaps(int a_count, int* a) {
    
    int numSwaps = 0, i, j, temp;
    
    for (i = 0; i < a_count; i++)
    {
        for (j = 0; j < a_count - 1; j++)
        {
            if (a[j] > a[j + 1])
            {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                numSwaps++;
            }
        }
    }
    
    printf("Array is sorted in %d swaps.\n", numSwaps);
    printf("First Element: %d\n", a[0]);
    printf("Last Element: %d\n", a[a_count - 1]);
}
