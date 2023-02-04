#include <stdbool.h>
#include <stdlib.h>

/**
 * Structure for the Singly Linked List
*/
typedef struct SinglyLinkedListNode {
    int data;
    SinglyLinkedListNode* next;
}SinglyLinkedListNode;

/**
 * has_cycle - finds if a linked list has a cycle using
 * Floyd's Cycle Detection Algorithm
 * @head: head of the linked list
 *
 * Return: If the linked list has a cycle, it returns true.
 * Otherwise, it returns false.
*/
bool has_cycle(SinglyLinkedListNode* head) {
    SinglyLinkedListNode *tortoise, *haire;

    tortoise = head, haire = head;
    while (haire != NULL)
    {
        haire = haire->next;
        if (haire != NULL)
            haire = haire->next, tortoise = tortoise->next;
        if (haire == tortoise)
            return true;
    }
    return false;
}
