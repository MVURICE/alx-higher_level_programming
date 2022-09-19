#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *p1;
	listint_t *prev;

	p1 = list;
	prev = list;
	while (list && p1 && p1->next)
	{
		list = list->next;
		p1 = p1->next->next;

		if (list == p1)
		{
			list = prev;
			prev =  p1;
			while (1)
			{
				p1 = prev;
				while (p1->next != list && p1->next != prev)
				{
					p1 = p1->next;
				}
				if (p1->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
