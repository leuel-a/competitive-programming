#include "lists.h"

/**
 * reverseList - reverses a ListNode linked list
 * @head: address of the head node
 *
 * Return: On success, it returns the address of the head node
 * after the list has been reversed.
*/
struct ListNode* reverseList(struct ListNode* head)
{
    struct ListNode *curr, *prev, *next;

    if (head == NULL)
        return (NULL);

    curr = head;
    prev = NULL;
    while (curr != NULL)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    head = prev;
    return (head);
}
