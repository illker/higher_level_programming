#include "lists.h"

/**
 * print_name - prototype function
 * @head: Variable char pointer
 * Return: 1
 */

int is_palindrome(listint_t **head)
{
	int a = 0, buffer[2048];

	if (head == NULL || *head == NULL)
		return (1);

	while(*head != NULL)
	{
		buffer[a] = (*head)->n;
		head = &(*head)->next;
        a++;
	}
	return (0)
}
