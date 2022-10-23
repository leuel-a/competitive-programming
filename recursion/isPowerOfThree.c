/**
 * isPowerOfThree - checks whether a number is a power of three
 * @n: the number to be checked
 *
 * Description:
 * 	Given an integer n, return true if it is a power of three.
 * 	Otherwise, return false.
 *
 * Return: If the number is a power of three, it returns true. If
 * not, it returns false.
 */
bool isPowerOfThree(int n){

    if (n == 1)
        return true;
    else if (n % 3 != 0 || n <= 0)
        return false;
    else
        return isPowerOfThree(n / 3);
}

