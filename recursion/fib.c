#include "main.h"

/**
 * fib - finds the fibionaci number of the number passed as seq
 * @n: the number passed
 *
 * Description:
 *              F(0) = 0, F(1) = 1
 *              F(n) = F(n - 1) + F(n - 2), for n > 1.
 * Return: On success, it returns the number calculated
*/
int fib(int n)
{
    if (n == 0)
        return (0);
    else if (n == 1)
        return (1);
    return (fib(n - 1) + fib(n - 2));
}
