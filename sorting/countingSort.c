
/**
 * countingSort - this function will implement the Counting Sort 
 *
 * @arr_count: the sie of the array
 * @arr: the array to be sorted
 * @result_count: the size of the array to be returned
 *
 * Description: this function wont fully implement the Counting Sort
 * Algorithm rather it will only find the Frequecny Array
 * 	Frequency Array: this array will hold the frequecy of the array
 * 		that will be sorted. It has a default size of 100.
 *
 * Return: On success, it returns the frequecny array
 */
int* countingSort(int arr_count, int* arr, int* result_count) {
    
    int *frequency, i;
    
    *result_count = 100;
    frequency = malloc(sizeof(int) * (*result_count));
    for (i = 0; i < (*result_count); i++)
        frequency[i] = 0;
    for (i = 0; i < arr_count; i++)
        frequency[arr[i]]++;
    
    return frequency;    
}

