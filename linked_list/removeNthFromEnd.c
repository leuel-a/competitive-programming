#include "lists.h"

/**
 * removeNthFromEnd - removes the Nth node from the end of a ListNode linked list
 * @head: the address of the head node
 * @n: the node to be removed
 *
 * Return: It returns the address of the head node after the nth node from the end
 * is removed.
*/
struct ListNode* removeNthFromEnd(struct ListNode* head, int n)
{
    struct ListNode *curr, *prev;
    int sizeOfList, nth, i;

    curr = head, sizeOfList = 0;
    while (curr != NULL)
        curr = curr->next, sizeOfList++;
    nth = sizeOfList - n + 1;

    i = 0, curr = head, prev = NULL;
    while (curr != NULL && i != nth - 1)
        prev = curr, curr = curr->next, i++;

    if (prev == NULL)
        head = curr->next;
    else
    {
        if (curr->next)
            prev->next = curr->next;
        else
            prev->next = NULL;
    }
    return (head);
}
