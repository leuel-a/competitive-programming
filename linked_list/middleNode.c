#include "lists.h"

/**
 * middleNode - finds the middle node of a ListNode linked list
 * @head: address of the head node
 *
 * Return: On success, it returns the address of the head node
*/
struct ListNode* middleNode(struct ListNode* head)
{
    int sizeOfList, middleOfList, i;
    struct ListNode *aux;

    aux = head, sizeOfList = 0;
    while (aux != NULL)
        aux = aux->next, sizeOfList++;
    middleOfList = sizeOfList / 2 + 1;

    aux = head, i = 0;
    while (aux != NULL && i != middleOfList - 1)
        aux = aux->next, ++i;
    return aux;
}

