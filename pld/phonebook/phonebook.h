#ifndef PHONEBOOK_H
#define PHONEBOOK_H

#include <stdio.h>
#include <string.h>
#include <cs50.h>

typedef struct
{
	char *phone_name;
	char *phone_number;
} person;

void draw(int n);

#endif /* PHONEBOOK_H */
