#include "lists.h"

/**
 * check_cycle - check cycle
 * description: does a singly linked list have a cycle
 * @list: list
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *s_p = list, *f_p = list;

	while (s_p && f_p && f_p->next)
	{
		s_p = s_p->next;
		f_p = f_p->next;
		if (s_p == f_p)
		{
			return (1);
		}
		else
		{
			return (0);
		}
	}
	return(0);
}
