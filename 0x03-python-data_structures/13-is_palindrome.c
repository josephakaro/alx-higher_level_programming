#include "lists.h"

/**
 * is_palindrome - tests if linked lists is (palindrome)
 *
 *  @head: address of pointer(head) to list
 *
 * Return: 1 is (palindrome) else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *last = *head, *first = *head, *nod, *pr;
	int error = 0;

	while (first != NULL && first->next != NULL)
	{
		first = first->next->next;
		last = last->next;
	}
	nod = last;
	pr = NULL;
	while (nod)
	{
		first = nod->next;
		nod->next = pr;
		pr = nod;
		nod = first;
	}
	first = *head;
	nod = pr;
	while (pr)
	{
		if (first->n != pr->n)
		{
			error = 1;
			break;
		}
		first = first->next;
		pr = pr->next;
	}
	pr = NULL;
	while (nod)
	{
		first = nod->next;
		nod->next = pr;
		pr = nod;
		nod = first;
	}
	return (!error);
}