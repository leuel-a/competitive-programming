/**
 * middleNode - this function will find the middle node of a linked list
 * @head: this is the head of a linked list
 *
 * Description:
 * 	Given the head of a singly linked list, return the middle node of the linked list.
 * 		If there are two middle nodes, return the second middle node.
 *
 * 		Example: 
 * 			Input: head = [1,2,3,4,5]
 * 			Output: [3,4,5]
 * 			Explanation: The middle node of the list is node 3.
 *
 * Return: On success, it returns a pointer to the middle of the linked list.
 */

struct ListNode* middleNode(struct ListNode* head){
    
    struct ListNode* temp, *middle;
    int n = 0, i;
    
    temp = head;
    while (temp != NULL)
    {
        n = n + 1;
        temp = temp->next;
    }
    
    temp = head;
    i = 0;
    while (temp != NULL)
    {
        if (i == (n/2))
        {
            middle = temp;
            break;
        }
        i++;
        temp = temp->next;
    }
    return middle;
}
