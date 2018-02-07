#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>

#define MAX_REQUEST_LENGTH 256
#define QUIT 0
#define SAVE_QUIT 1

char request_buffer[MAX_REQUEST_LENGTH];

void get_user_request()
{
	puts("(r)ead,[offset] or (w)rite,[offset],[value], (s)ave/quit or (q)uit: ");
	fgets(request_buffer, MAX_REQUEST_LENGTH, stdin);
}

int user_interaction(unsigned char * file_buffer)
{
	long long offset;
	int value;

	do {
		get_user_request();

		if (request_buffer[0] == 'r')
		{
			if (sscanf(request_buffer, "r,%lld\n", &offset) == 1)
				printf("%#2.2d\n", file_buffer[offset]);
			else
				puts("error: unrecognized option");
		}
		else if (request_buffer[0] == 'w')
		{
			if (sscanf(request_buffer, "w,%lld,%d\n", &offset, &value) == 2)
				file_buffer[offset] = value;
			else
				puts("error: unrecognized option");
		} 
		else if (request_buffer[0] == 'q' || request_buffer[0] == 's')
		{
			puts("exiting application");
		}
		else
		{
			puts("error: unrecognized option");
		}

	} while (request_buffer[0] != 'q' && request_buffer[0] != 's');

	return (request_buffer[0] == 'q')? QUIT : SAVE_QUIT;
}

void launch(int file_descriptor, long long file_size)
{
	unsigned char file_buffer[file_size];

	if (read(file_descriptor, file_buffer, file_size) != file_size)
	{
		fprintf(stderr, "error: couldn't read file contents\n");
		exit(EXIT_FAILURE);
	}

	if (user_interaction(file_buffer) == SAVE_QUIT)
	{
		lseek(file_descriptor, 0, SEEK_SET);
		if (write(file_descriptor, file_buffer, file_size) != file_size)
			fprintf(stderr, "warning: write error\n");
	}

	close(file_descriptor);		
}

long long get_file_size(int file_descriptor)
{
	struct stat stat_struct;

	if (fstat(file_descriptor, &stat_struct) == -1)
	{
		fprintf(stderr, "error: cannot stat given file\n");
		exit(EXIT_FAILURE);
	}

	return(stat_struct.st_size);	
}

int main(int argc, char * argv[])
{
	int input_file_fd;
	long long input_file_size;

	if (argc != 2)
	{
		fprintf(stderr, "usage: %s [filename]\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	if ((input_file_fd = open(argv[1], O_RDWR)) == -1)
	{
		fprintf(stderr, "error opening file %s\n", argv[1]);
		exit(EXIT_FAILURE);
	}

	input_file_size = get_file_size(input_file_fd);
	launch(input_file_fd, input_file_size);	

	return(0);
}
