#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "HashTable.h"

struct buckets;

struct HashTableObjectTag
{
	int sentinel;
    int numBuckets;
    int numEntries;
    struct buckets ** arraybucketPTR;
    HashTableInfo * hashTableInfo;
};

int main()
{
	int success = 0;
	char command[20];
	struct HashTableObjectTag * newHashTable;
	
	fprintf(stdout, "Welcome to the Dynamic Dictionary! I shall take care of all your storing needs.\n");
	fprintf(stdout, "To start, I recommend creating a new HashTableObject.\n");
	fprintf(stdout, "Available commands include: create, destroy, insert, delete, find, setbehaviour, getInfo, quit\n");
	
	while(1)
	{
		fprintf(stdout, "Command: ");
		fscanf(stdin, "%s", command);
		
		if(strcmp(command, "create") == 0)
		{
			int initialSize;
			fprintf(stdout, "What would you like the initial size to be? \n");
			fscanf(stdin, "%d", &initialSize);
					
			if(CreateHashTable(&newHashTable, (unsigned int)initialSize) == 0)
			{
				success = 1;
				fprintf(stdout, "Create was successful!\n");
				continue;
			}
			else
			{
				fprintf(stdout, "Create Failed!\n");
				continue;
			}
		}
		
		//No HashTableObject created
		if(success == 0)
		{
			fprintf(stdout, "Cannot be done without a HashTableObject.\n");
			continue;
		}
		
		//Dynamic behaviour is false (nothing happens)
		
		//Dynamic behaviour is true
			
		if(strcmp(command, "print") == 0)
		{
			char ** keyArrayPTR;
			unsigned int keyCount;
			int status = GetKeys(newHashTable, &keyArrayPTR, &keyCount);

			if (status == -1) 
				continue;
		
			for (int i = 0; i < newHashTable->numEntries; i++)
			{
				char * dat;
				char * key = *((keyArrayPTR) + i);
				FindEntry(newHashTable, key, (void**) &dat);
				fprintf(stdout, "%s:%s\n", key, dat);
				free(key);
			}
			free(keyArrayPTR);
		}
		
		if(strcmp(command, "check") == 0)
		{
			fprintf(stdout, "Entry Count: %d\n", newHashTable->numEntries);
			fprintf(stdout, "Bucket Count: %d\n", newHashTable->numBuckets);
		}
		
		if(strcmp(command, "setBehaviour") == 0)
		{
			int dynamicBehaviour;
			float expandUseFactor;
			float contractUseFactor;
			fprintf(stdout, "Dynamic (1) or Static (0)?\n");
			fscanf(stdin, "%d", &dynamicBehaviour);
			fprintf(stdout, "Enter expandUseFactor: \n");
			fscanf(stdin, "%f", &expandUseFactor);
			fprintf(stdout, "Enter contractUseFactor: \n");
			fscanf(stdin, "%f", &contractUseFactor);
			
			if(SetResizeBehaviour(newHashTable, dynamicBehaviour, expandUseFactor, contractUseFactor) == 0)
			{
				fprintf(stdout, "Changes were successful!\n");
				fprintf(stdout, "Dynamics Behaviour: %d\n", (newHashTable->hashTableInfo)->dynamicBehaviour);
				fprintf(stdout, "Expand Use Factor: %.02f\n", (newHashTable->hashTableInfo)->expandUseFactor);
				fprintf(stdout, "Contract Use Factor: %.02f\n", (newHashTable->hashTableInfo)->contractUseFactor);
				continue;
			}
			else
			{
				fprintf(stdout, "Failure to make changes!\n");
				continue;
			}
		}
				
		//print out hash table info
		if (!strcmp(command, "info")) {
			HashTableInfo * info;
			info = malloc(sizeof(HashTableInfo));
			int success = GetHashTableInfo(newHashTable, info);
			if (success<0) {
				printf("need to create a valid hash table\n");
			}
			else {
				printf("bucketCount: %d\n", info->bucketCount);
				printf("loadFactor: %.2f\n", info->loadFactor);
				printf("useFactor: %.2f\n", info->useFactor);
				printf("largestBucketSize: %d\n", info->largestBucketSize);
				printf("dynamicBehaviour: %d\n", info->dynamicBehaviour);
				printf("expandUseFactor: %.2f\n", info->expandUseFactor);
				printf("contractUseFactor: %.2f\n", info->contractUseFactor);
			}
			free(info);
		}	
		
		if (strcmp(command, "insert") == 0) 
		{
			char * key = malloc(81 * sizeof(char));
			char * value = malloc(81 * sizeof(char));
			fprintf(stdout, "Key: ");
			fscanf(stdin, " %80s", key);
			fprintf(stdout, "Value: ");
			fscanf(stdin, " %80s", value);
			char * existingData = NULL;
			int result = InsertEntry(newHashTable, key, value, (void**) &existingData);
					
			switch(result){
				case 0:
					fprintf(stdout, "Inserted into blank space.\n");
					free(key);
					break;
				case 1:
					fprintf(stdout, "Inserted after resolving hash collision.\n");
					free(key);
					break;
				case 2:
					fprintf(stdout, "Exists: %s\nInserted after removing existing data: %s.\n", existingData, existingData);
					free(existingData);
					free(key);
					break;
				default:
					fprintf(stdout, "InsertEntry failed!\n");
					free(key);
					break;
			}
		} 
		
		else if (strcmp(command, "find") == 0)
		{ 
			char key[81];
			char * value;
			printf("Key: ");
			scanf(" %80s", key);
					
			int success = FindEntry(newHashTable, key, (void**) &value);
			if (success == 0)
				fprintf(stdout, "%s\n", value);			
			else
				fprintf(stdout, "readPosition returned failure\n");
		} 
				
		else if (strcmp(command, "delete") == 0) 
		{
			fprintf(stdout, "Key: ");
			char key[81];
			scanf(" %80s", key);
			char * value;
			int success = DeleteEntry(newHashTable, key, (void**) &value);
			
			if (success == 0) {
				printf("Deleted (was %s)\n", value);
				free(value);
			} 
			
			else {
				printf("DeleteValue returned failure\n");
			}
		} 
		
		if(strcmp(command, "destroy") == 0)
		{
			fprintf(stdout, "Destroy was successful!\n");
		}		
				
		if(strcmp(command, "quit") == 0)
		{
			DestroyHashTable(&newHashTable);
			fprintf(stdout, "Quit was successful!\n");
			return 0;
		}
	}
}
