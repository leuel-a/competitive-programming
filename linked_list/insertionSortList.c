#include "lists.h"

/**
 * insertionSortList - sorts a singly linked list using the insertion sort
 * algorithm
 * @head: address of the head node to be sorted
 *
 * Return: On success, it returns the address of the head node of the now sorted
 * linked list.
*/
struct ListNode* insertionSortList(struct ListNode* head)
{
    struct ListNode *sorted, *next, *aux, *prev;

    sorted = NULL, prev = NULL;
    while (head != NULL)
    {
        next = head->next;
        if (sorted == NULL)
            head->next = sorted, sorted = head;
        else
        {
            aux = sorted;
            while (aux != NULL && aux->val <= head->val)
                prev = aux, aux = aux->next;

            if (prev == NULL)
                head->next = aux, sorted = head;
            else
                prev->next = head, head->next = aux;
        }
        head = next, prev = NULL;
    }
    return (sorted);
}
