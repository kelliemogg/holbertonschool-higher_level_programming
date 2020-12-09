#include "lists.h"

/**
 * check_cycle - check cycle
 * description: does a singly linked list have a cycle
 * @list: list
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list->next;

	if (list == NULL)
		return(0);
	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
			return(1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return(0);
}
