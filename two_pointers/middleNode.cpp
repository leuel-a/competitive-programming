#include <iostream>

/**
 * Definition for singly-linked list
*/
struct ListNode {
    int val;
    ListNode *next;
};

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode *slow, *fast;

        slow = head, fast = head;
        while (fast != NULL && fast->next != NULL)
            slow = slow->next, fast = fast->next->next;
        return slow;
    }
};
