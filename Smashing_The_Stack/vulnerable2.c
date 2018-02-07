#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXIMUM_TWEETS 528

struct live_feed {
	double tweets;
	double retweets;
	int update;
};

void launch(char * cursor, int feed_count)
{
	struct live_feed buffer[MAXIMUM_TWEETS];
	
	if (feed_count < MAXIMUM_TWEETS) 
	{       
		memcpy(buffer, cursor, feed_count * sizeof(struct live_feed));
	}
}

int main(int argc, char * argv[])
{
	int feed_count;
	char * cursor;
	
	if (argc != 2)
	{
		fprintf(stderr, "Usage: %s [number of tweets],[data]\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	feed_count = strtoul(argv[1], &cursor, 10);
	
	if ((*cursor != ',') || (strlen(cursor + 1) < sizeof(struct live_feed) * feed_count))
	{
		fprintf(stderr, "Usage: %s [number of tweets],[data]\n", argv[0]);
		exit(EXIT_FAILURE);		
	}

	cursor = cursor + 1;	
	launch(cursor, feed_count);
	return(0);
}
