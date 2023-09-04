#include "lists.h"

/**
 * check_cycle - checks for linked list cycle
 * @list: Checker
 * Return: 0 none cycle, 1 on cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *last = list;
	listint_t *first = list;
	listint_t *last_visited = NULL;

	if (list == NULL)
		return (0);

	while (first && first->next)
	{
		last = last->next;
		first = first->next->next;

		if (first == last || first == last_visited)
			return (1);

		last_visited = last;
	}
	return (0);
}
