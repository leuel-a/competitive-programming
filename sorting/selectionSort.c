int select(int arr[], int i)
{
    return 0;
}


void selectionSort(int arr[], int n)
{
    int i, jMin, j;
    
    for (i = 0; i < n - 1; i++)
    {
        jMin = i;
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[jMin])
                jMin = j;
        }
        if (jMin != i)
        {
            int temp = arr[jMin];
            arr[jMin] = arr[i];
            arr[i] = temp;
        }
        
    }
}
