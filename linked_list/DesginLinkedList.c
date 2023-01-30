#include <stdio.h>
#include <stdlib.h>

/**
 * Structure for a singly linked list
*/
struct node{
    int n;
    struct node *next;
};

/**
 * Structure for the head of a linked list
*/
typedef struct {
    struct node *root;
} MyLinkedList;

/**
 * Linked List Functions
*/
void printList(const MyLinkedList *head);
MyLinkedList* myLinkedListCreate();
void myLinkedListAddAtHead(MyLinkedList* obj, int val);
void myLinkedListAddAtTail(MyLinkedList* obj, int val);
int myLinkedListGet(MyLinkedList* obj, int index);
void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val);
void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index);
void myLinkedListFree(MyLinkedList* obj);

/**
 * main - Entry point of program
 *
 * Return: Nothing
*/
int main(void)
{
    MyLinkedList *obj;
    int get;

    obj = myLinkedListCreate();
    myLinkedListAddAtHead(obj, 7);
    myLinkedListAddAtHead(obj, 2);
    myLinkedListAddAtHead(obj, 1);
    myLinkedListAddAtIndex(obj, 3, 0);
    myLinkedListDeleteAtIndex(obj, 2);
    myLinkedListAddAtHead(obj, 6);
    myLinkedListAddAtTail(obj, 4);

    get = myLinkedListGet(obj, 4);
    printf("%d\n\n", get);

    printList(obj);
    return (0);
}

/**
 * printList - prints a single linked list
 * @head: address of the head node
 *
 * Return: Nothing
*/
void printList(const MyLinkedList *head)
{
    struct node *aux;
    if (head->root == NULL)
        return;

    aux = head->root;
    while (aux != NULL)
    {
        printf("%d\n", aux->n);
        aux = aux->next;
    }
}

/**
 * myLinkedListCreate - creates a new linked list
 *
 * Return: On success, it returns the address of the head node
 * of the new linked list. On error, it returns NULL.
*/
MyLinkedList* myLinkedListCreate()
{
    MyLinkedList *head;

    head = malloc(sizeof(MyLinkedList));
    if (head == NULL)
        return (NULL);
    head->root = NULL;
    return (head);
}

/**
 * myLinkedListAddAtTail - adds a new node at the head of the
 * given linked list.
 * @obj: address of the head node
 * @val: value of the head node
 *
 * Return: Nothing
*/
void myLinkedListAddAtHead(MyLinkedList* obj, int val)
{
    struct node *new;

    new = malloc(sizeof(struct node));
    if (new == NULL)
        return;
    new->n = val;

    if (obj->root == NULL)
        obj->root = new, new->next = NULL;
    else
        new->next = obj->root, obj->root = new;
}

/**
 * myLinkedListAddAtTail - adds a new node at the tail of the
 * given linked list.
 * @obj: address of the head node
 * @val: value of the head node
 *
 * Return: Nothing
*/
void myLinkedListAddAtTail(MyLinkedList* obj, int val)
{
    struct node *new, *aux;

    new = malloc(sizeof(struct node));
    if (new == NULL)
        return;
    new->n = val;
    new->next = NULL;
    if (obj->root == NULL)
        obj->root = new;
    else
    {
        aux = obj->root;
        while (aux->next != NULL)
            aux = aux->next;
        aux->next = new;
    }
}

/**
 * myLinkedListGet - gets that value of a linked list at a certain index
 * @obj: address of the head node of the list
 * @index: index to be found
 *
 * Return: On success, it returns the value at the certaing index. On error,
 * it returns -1, but errno is not set appropriately
*/
int myLinkedListGet(MyLinkedList* obj, int index)
{
    struct node *aux;
    int i = 0;

    aux = obj->root;
    while (aux != NULL && i <= index)
    {
        if (i == index)
            return (aux->n);
        i++, aux = aux->next;
    }
    return (-1);
}

/**
 * myLinkedListAddAtIndex - adds a new node at the given index
 * @obj: address of the head node
 * @index: index to be added at
 * @val: value of the new node
 *
 * Return: Always nothing.
*/
void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val)
{
    struct node *new, *aux, *prev;
    int i = 0;

    aux = obj->root, prev = NULL;
    while (aux != NULL && i <= index)
    {
        if (i == index)
        {
            new = malloc(sizeof(struct node));
            if (new == NULL)
                return;
            new->n = val;

            if (prev == NULL)
                new->next = aux, obj->root = new;
            else
                prev->next = new, new->next = aux;
        }
        i++, prev = aux, aux = aux->next;
    }
    if (i == index)
    {
        new = malloc(sizeof(struct node));
        if (new == NULL)
            return;
        new->n = val;

        if (prev == NULL)
            new->next = aux, obj->root = new;
        else
            prev->next = new, new->next = NULL;
    }
}

/**
 * myLinkedListDeleteAtIndex - deletes a node at a given index
 * @obj: address of the head node
 * @index: index of the node to be deleted at
 *
 * Return: Always nothing.
*/
void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index)
{
    struct node *aux, *prev, *next;
    int i = 0;

    aux = obj->root, prev = NULL;
    while (aux != NULL && i <= index)
    {
        if (i == index)
        {
            next = aux->next;
            free(aux);

            if (prev == NULL)
                obj->root = next;
            else
                prev->next = next;
            break;
        }
        i++, prev = aux, aux = aux->next;
    }
}

/**
 * myLinkedListFree - frees a linked list
 * @obj: address of the head node to be freed
*/
void myLinkedListFree(MyLinkedList* obj)
{
    struct node *temp;

    while (obj->root != NULL)
    {
        temp = obj->root;
        obj->root = obj->root->next;
        free(temp);
    }
    obj->root = NULL;
}
