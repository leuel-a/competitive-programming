#include "lists.h"

/**
 * deleteDuplicates - removes duplicates from a sorted linked list
 * @head: address of the head node
 *
 * Return: On success, it returns the address of the head of the sorted
 * non-duplicate linked list.
*/
struct ListNode* deleteDuplicates(struct ListNode* head)
{
    struct ListNode *uniqueHead, *uniqueTail, *temp;

    if (!head)
        return (NULL);
    uniqueHead = head;
    head = head->next;
    uniqueTail = uniqueHead;
    while (head != NULL)
    {
        if (uniqueTail->val != head->val)
        {
            temp = head, head = head->next;
            uniqueTail->next = temp;
            uniqueTail = temp;
        } else {
            head = head->next;
        }
    }
    uniqueTail->next = NULL;
    return (uniqueHead);
}
