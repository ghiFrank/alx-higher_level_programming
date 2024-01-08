#include "lists.h"
/**
 * is_palindrom - if plaindrom is recu
 * @head: head list
 * Return: 0 if not pali, 1 if is pali
*/
int is_palindrom(listint_t **head)
{
    if (head == NULL || *head == NULL)
        return (1);
    return (aux_palind(head, *head));
}
/**
 * aux_palind - funct to know if is palindrome
 * @head: head list
 * @end: end list
*/
int aux_palind(listint_t **head, listint_t *end)
{
    if (end == NULL)
        return (1);
    if (aux_palind(head, end->next) && (*head)->n == end->n)
    {
        *head = (*head)->next;
        return (1);
    }
    return (0);
}
