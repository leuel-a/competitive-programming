/**
 * isPowerOfFour - checks whether a number is a power of four
 * @n: to be checked
 *
 * Description:
 * 	Given an integer n, return true if it is a power of four.
 * 	Otherwise, return false.
 * Return: If the number is a power of four, it returns true. If
 * not, it returns false.
 */
bool isPowerOfFour(int n){

    if (n == 1)
        return true;
    else if (n % 4 != 0 || n <= 0)
        return false;
    else
        return isPowerOfFour(n / 4);
}
