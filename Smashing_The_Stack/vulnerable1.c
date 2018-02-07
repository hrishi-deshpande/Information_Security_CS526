#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 200

void launch(char * user_argument)
{
	char buffer[BUFFER_SIZE];
	strcpy(buffer, user_argument);
}

int main(int argc, char * argv[])
{
	if (argc != 2)
	{
		fprintf(stderr, "Usage: %s ARGUMENT\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	launch(argv[1]);
	return(0);
}
