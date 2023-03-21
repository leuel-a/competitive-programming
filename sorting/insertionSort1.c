
/**
 * insertionSort1 - this function will place the last element
 * of an array in the correct position.
 *
 * Description: This is not a full implementation of an insertion
 * 	sort. Rather, only the last element in the array is not in
 * 	the right place, the rest are sorted
 *
 * @n: the size of the array
 * @arr_count: the size of the array
 * @arr: the array to be sorted
 *
 * Return: Nothing
 */
void insertionSort1(int n, int arr_count, int* arr) {
    
    int last, i , j;
    
    i = n - 2;
    last = arr[n - 1];    
    while (i >= 0 && arr[i] > last)
    {
        arr[i + 1] = arr[i];
        for (j = 0; j < arr_count; j++)
            printf("%d ",  arr[j]);
        putchar('\n');
        i--;
    }
    arr[i + 1] = last;
    for (j = 0; j < arr_count; j++)
        printf("%d ",  arr[j]);
    putchar('\n');
}
