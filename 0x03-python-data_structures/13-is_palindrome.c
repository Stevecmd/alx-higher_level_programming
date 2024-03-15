#include <stddef.h>  /* Include <stddef.h> for size_t */
#include "lists.h"
#include <stdlib.h>  /* Include <stdlib.h> for malloc and free */

#ifndef NULL
#define NULL ((void *)0)
#endif

/**
 * list_len - finds the number of elements in a linked list.
 * @h: pointer to the head of the linked list.
 *
 * Return: number of elements in the linked list.
 */
size_t list_len(listint_t *h)
{
    size_t  nodes = 0;

    if (h == NULL)
        return (0);

    while (h != NULL)
    {
        nodes++;
        h = h->next;
    }

    return (nodes);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    int *nArr, i = 0, j = 0, len = 0;
    listint_t *temp;

    if (*head == NULL)
        return (1);  /* Empty list is palindrome */

    temp = *head;
    len = list_len(temp);

    /* Allocate memory to store the values of nodes in the linked list */
    nArr = (int *)malloc(sizeof(int) * len);
    if (nArr == NULL)
        return (0);  /* Return 0 if memory allocation fails */

    temp = *head;
    while (temp != NULL)
    {
        nArr[j] = temp->n;  /* Store the value of each node in the array */
        j++;
        temp = temp->next;
    }

    /* Check if the values stored in the array form a palindrome */
    for (i = 0, j = len - 1; i < j; i++, j--)
    {
        if (nArr[i] != nArr[j])
        {
            free(nArr);
            return (0);
        }
    }

    free(nArr);
    return (1);
}
