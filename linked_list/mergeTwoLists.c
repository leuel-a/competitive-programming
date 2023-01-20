#include "lists.h"


/**
 * mergeTwoLists - merges two sorted ListNode linked lists
 * @list1: address of the head node of the first list
 * @list2: address of the head node of the second list
 *
 * Return: On success, the address of the new merged sorted list.
*/
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2)
{
    struct ListNode *mergedHead, *mergedTail, *temp;

    if (!list1 && !list2)
        return (NULL);

    if (!list1 && list2)
        mergedHead = list2, list2 = list2->next;
    else if (list1 && !list2)
        mergedHead = list1, list1 = list1->next;
    else if (list1->val <= list2->val)
        mergedHead = list1, list1 = list1->next;
    else
        mergedHead = list2, list2 = list2->next;

    mergedTail = mergedHead;
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->val <= list2->val)
            temp = list1, list1 = list1->next;
        else
            temp = list2, list2 = list2->next;

        mergedTail->next = temp;
        mergedTail = temp;
    }

    if (list1)
        mergedTail->next = list1;
    else if (list2)
        mergedTail->next = list2;
    return (mergedHead);
}
