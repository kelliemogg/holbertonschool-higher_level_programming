#include "lists.h"

/**
 * is_palindrome - pali?
 * description: is it a palindrome
 * @head: head of list
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *tail;

	if (*head == NULL)
		return (1);
	{
		tail = *head;
	while (tail->next != NULL)
		tail = tail->next;
	if (tail != *head)
		return (0);
	else
		return (1);
	}
	return (0);
}
