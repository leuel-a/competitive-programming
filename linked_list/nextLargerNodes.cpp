#include <iostream>
#include <stack>
#include <vector>
#include <ctype.h>
using std::vector, std::stack;

/**
 * Definition for singly-linked list
*/
struct ListNode {
    int n;
    ListNode *next;
};

void print_list(const ListNode *head);
ListNode *addnode_end(ListNode **head, int value);
vector<int> nextLargerNodes(ListNode* head);


/**
 * main - entry point of program
 *
 * Return: Always 0.
*/
int main(void)
{
    ListNode *head;

    head = NULL;
    addnode_end(&head, 2);
    addnode_end(&head, 1);
    addnode_end(&head, 5);
    print_list(head);
    std::putchar('\n');
    nextLargerNodes(head);
    return 0;
}

/**
 * print_list - prints a singly-linked list
 * @head: head node of the list to be printed
 *
 * Return: Nothing.
*/
void print_list(const ListNode *head)
{
    if (!head)
        return;
    while (head != NULL)
        std::printf("%d\n", head->n), head = head->next;
}

/**
 *
*/
ListNode *addnode_end(ListNode **head, int value)
{
    ListNode *temp, *aux;

    temp = (ListNode *)std::malloc(sizeof(ListNode));
    if (temp == NULL)
        return NULL;
    temp->n = value;
    temp->next = NULL;

    if (*head == NULL)
        *head = temp;
    else
    {
        aux = *head;
        while (aux->next != NULL)
            aux = aux->next;
        aux->next = temp;
    }
    return temp;
}

/**
 *
*/
vector<int> nextLargerNodes(ListNode* head)
{
    vector<int> nextGreater;
    stack<int> s;

    while (head != NULL)
    {
        if (s.empty() == true || s.top() > head->n)
            s.push(head->n);
        else
        {
            while (s.empty() == false && s.top() < head->n)
            {
                nextGreater.push_back(head->n);
                s.pop();
            }
            s.push(head->n);
        }
        head = head->next;
    }
}
