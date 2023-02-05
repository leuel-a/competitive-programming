#include <stdlib.h>
#include <stdio.h>

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    struct ListNode *next;
};

/**
 * deleteDuplicates - removes duplicates from a sorted linked list
 * @head: address of the head node
 *
 * Return: On success, it returns the address of the head of the sorted
 * non-duplicate linked list.
*/
struct ListNode* deleteDuplicates(struct ListNode* head)
{
    struct ListNode *aux, *prev, *curr;
    int value;

    prev = NULL, curr = head;
    while (curr != NULL)
    {
        value = curr->val, aux = curr->next;
        while (aux != NULL && aux->val == value)
            aux = aux->next;

        if (curr->next == aux)
            prev = curr, curr = curr->next;
        else if (prev == NULL)
            curr = aux, head = curr;
        else
            prev->next = aux, curr = aux;
    }
    return head;
}
