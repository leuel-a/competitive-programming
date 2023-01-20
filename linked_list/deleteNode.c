#include "lists.h"

/**
 * deleteNode - deletes a node in a ListNode linked list
 * @node: the address of the node to be removed
 *
 * Description:
 *      You are given the node to be deleted node. You will not be
 *      given access to the first node of head. All the values of the
 *      linked list are unique, and it is guaranteed that the given
 *      node node is not the last node in the linked list.
 *
 * Return: Always Nothing.
*/
void deleteNode(struct ListNode* node)
{
    struct ListNode *prev;

    while (node->next != NULL)
    {
        node->val = node->next->val;
        prev = node;
        node = node->next;
    }
    prev->next = NULL;
    free(node);
}
