#include <iostream>
#include <stack>
#include <vector>
#include <ctype.h>
using std::vector, std::stack;

/**
 * Definition for singly-linked list
*/
struct ListNode {
    int n;
    ListNode *next;
};
/**
 * nextLargerNodes - finds the next larger nodes in a linked list
 * @head: address of the head node of the linked list
 *
 * Return: On success, it returns the next larger nodes vector.
*/
vector<int> nextLargerNodes(ListNode* head)
{
    vector<int> nextGreater;
    stack<int> s;

    while (head != NULL)
    {
        if (s.empty() == true || s.top() > head->n)
            s.push(head->n);
        else
        {
            while (s.empty() == false && s.top() < head->n)
            {
                nextGreater.push_back(head->n);
                s.pop();
            }
            s.push(head->n);
        }
        head = head->next;
    }
}
