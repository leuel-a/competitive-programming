// ==============================================================================//
/**
 * gradingStudents - this function will grade the students based on the 
 * specifictation in HackerRank university 
 *
 * @grades_count: the number of grades that will be checked(size of grades_count)
 * @grades: this array is the grades of the student
 * @result_count: the size of the array that will be returned
 *
 * Description: 
 * 	HackerLand University has the following grading policy:
 * 		--> Every student receives a grade in the inclusive range from 0 to 100.
 * 		--> Any grade less than 40 is a failing grade.
 * 	Sam is a professor at the university and likes to round each student's  according
 * 		 to these rules:
 * 		--> If the difference between the grade and the next multiple of 5  is 
 * 			less than 3, round grade up to the next multiple of 5.
 * 		--> If the value of grade is less than 38, no rounding occurs as the 
 * 			result will still be a failing grade.
 *
 * Return: On success, it returns the new grades with the rounded values
 */

int* gradingStudents(int grades_count, int* grades, int* result_count) {
    
    int *new_grades, aux, i, diff;
    
    *result_count = grades_count;
    new_grades = malloc(sizeof(int) * *result_count);
    for (i = 0; i < grades_count; i++)
    {
        if (grades[i] < 38){
            new_grades[i] = grades[i];
            continue;
        }
        aux = grades[i];
        while (aux % 5 != 0)
            aux = aux + 1;
        diff = aux - grades[i];
        
        if (diff < 3){
            new_grades[i] = aux;
        } else {
            new_grades[i] = grades[i];   
        }
    }
    return (new_grades);
}
