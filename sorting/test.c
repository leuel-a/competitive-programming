#include "stdio.h"
#include <string.h>

int main(void)
{
	char s[] = "is2 sentence4 This1 a3", *words[9], *token, *temp, *sorted[9];
	int i, last;

	temp = strdup(s);
	i = 0;
	token = strtok(temp, " ");
	while (token != NULL)
	{
		words[i] = token;
		token = strtok(NULL, " ");
		i++;
	}

	for (i = 0; words[i] != NULL; i++)
	{
		last = (words[i])[strlen(words[i]) - 1] - '0';
		sorted[last - 1] = words[i];

	}

	for(i = 0; sorted[i] != NULL; i++)
		puts(sorted[i]);

	strcat(sorted[0], sorted[1]);
	puts(sorted[0]);
	return (0);
}
