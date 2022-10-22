/**
 * isValid - checks if s is a valid string
 *
 * Description:
 * 	Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 * 		An input string is valid if:
 * 			- Open brackets must be closed by the same type of brackets.
 * 			- Open brackets must be closed in the correct order.
 * 			- Every close bracket has a corresponding open bracket of the same type.
 *
 * Return: If the string is a valid string, it returns true. If not it returns false.
 */
bool isValid(char * s){
    
    int i = 0, top;
    char stack[100000];
    
    top = -1;
    while (s[i] != '\0')
    {
        if (s[i] == '{' || s[i] == '[' || s[i] == '(')
        {
            top++;
            stack[top] = s[i];
        } else if (top != -1 && s[i] == '}' && stack[top] == '{')
            top--;
        else if (top != -1 && s[i] == ']' && stack[top] == '[')
            top--;
        else if (top != -1 && s[i] == ')' && stack[top] == '(')
            top--;
        else
            return false;
        i++;
    }
    if (top != -1)
        return false;
    return true;
}
