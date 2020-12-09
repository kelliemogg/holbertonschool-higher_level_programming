#include "lists.h"

/**
 * check_cycle - check cycle
 * description: does a singly linked list have a cycle
 * @list: list
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL)
		return(0);

	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		fast = fast->next->next;
                slow = slow->next;

		if (fast == slow)
			return(1);
	}
	return(0);
}
