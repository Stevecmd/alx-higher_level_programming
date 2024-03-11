#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - Checks if a singly-linked list contains a cycle.
  * @head: A pointer to the head of the singly-linked list.
  *
  * Return: 1 if there is a cycle, 0 otherwise.
  */

int check_cycle(listint_t *head)
{
	listint_t *slow_runner, *fast_runner;

	if (head == NULL || head->next == NULL)
		return (0);

	slow_runner = head->next;
	fast_runner = head->next->next;

	while (slow_runner && fast_runner && fast_runner->next)
	{
		if (slow_runner == fast_runner)
			return (1);

		slow_runner = slow_runner->next;
		fast_runner = fast_runner->next->next;
	}

	return (0);
}
