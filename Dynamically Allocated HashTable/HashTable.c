#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "HashTable.h"

struct buckets
{
	char *key;
    char *value;
    struct buckets *left;
    struct buckets *right; 
};

typedef struct buckets treeNode;

struct HashTableObjectTag
{
	int sentinel;
    int numBuckets;
    int numEntries;
    struct buckets ** arraybucketPTR;
    HashTableInfo * hashTableInfo;
};

int SimpleIntHash(char *input, int range)
{
	int hashedkey = 0;
	while(*input != '\0')
	{
		hashedkey += (int)(*input);
		input ++;
	}
	return hashedkey % range;
}

void UseFactor(HashTablePTR *hashTableHandle)
{
	int usedBuckets = 0;
	for(int i = 0; i < (*hashTableHandle)->numBuckets; i++)
	{
		if( *((*hashTableHandle)->arraybucketPTR + i) != NULL)
			usedBuckets ++;
		fprintf(stdout,"Number of used Buckets is %d", usedBuckets);
	}
	((*hashTableHandle)->hashTableInfo)->useFactor = (float)usedBuckets/(*hashTableHandle)->numBuckets;
}

int CreateHashTable( HashTablePTR *hashTableHandle, unsigned int initialSize )
{
	(*hashTableHandle) = malloc(sizeof(HashTableObject)); //Allocates sufficient memory
	if(*hashTableHandle == NULL) //Checks to see if allocation was successful
		return -1;
		    
    (*hashTableHandle)->sentinel = (int)0xDEADBEEF;
    (*hashTableHandle)->numBuckets = (int)initialSize;
    (*hashTableHandle)->numEntries = 0;
    (*hashTableHandle)->arraybucketPTR = malloc(sizeof(struct buckets *) * initialSize);
    //Sufficient memory will be allocated to array of pointers to struct buckets
    
    for(int i = 0; i < initialSize; i++)
        *((*hashTableHandle)->arraybucketPTR + i) = NULL;
    //Set all pointers to Null
    
    (*hashTableHandle)->hashTableInfo = malloc(sizeof(HashTableInfo));
    //Allocate enough memory to store teh hashTableInfoObject
    SetResizeBehaviour( *hashTableHandle, 1, (float)0.7, (float)0.2);    
	((*hashTableHandle)->hashTableInfo)->bucketCount = (unsigned int)(*hashTableHandle)->numBuckets;
	((*hashTableHandle)->hashTableInfo)->loadFactor = (float)((*hashTableHandle)->numEntries)/((*hashTableHandle)->numBuckets);

	return 0;
	
	
	return 0;
}

void FreeBucket(treeNode * root)
{
	if(root != NULL)
	{
		FreeBucket(root->left);
		FreeBucket(root->right);
		free(root->key);
		free(root->value); //Set Null or not?
		free(root);
	}
}

int DestroyHashTable( HashTablePTR *hashTableHandle )
{
	if((*hashTableHandle)->sentinel != (int)0xDEADBEEF)
		return -1;
			
	for(int i = 0; i < (*hashTableHandle)->numBuckets; i++) //Free each bucket
	{
		treeNode * tempptr = *((*hashTableHandle)->arraybucketPTR + i);
		if(	tempptr == NULL) //Empty bucket, skip to next bucket
			continue;
		else FreeBucket(tempptr); //Free entire bucket
	}
	
	free( (*hashTableHandle)->arraybucketPTR); //Free array of pointers
	free(*hashTableHandle); //Free hashTableObject
	hashTableHandle = NULL;
	return 0;
}

////////////////////////////////////////////////////////////////////////////

void BucketCount(treeNode * root, int * count)
{
	if(root != NULL)
	{
		BucketCount(root->left, count);
		BucketCount(root->right, count);
		(*count) ++;
	}
}

int GetHashTableInfo( HashTablePTR hashTable, HashTableInfo *pHashTableInfo )
{
	if(hashTable->sentinel != (int)0xDEADBEEF)
		return -1;
		
	pHashTableInfo->bucketCount = (unsigned int)hashTable->numBuckets;
	pHashTableInfo->loadFactor = (float)(hashTable->numEntries)/(hashTable->numBuckets);
    int largestBucketSize = 0;
    int currentBucketSize = 0;
    for(int i = 0; i < hashTable->numBuckets; i++)
    {
		currentBucketSize = 0;
		//Count the number of items in the ith bucket
		BucketCount( *(hashTable->arraybucketPTR + i), &currentBucketSize);
		if(currentBucketSize > largestBucketSize)
			largestBucketSize = currentBucketSize;
	}
    pHashTableInfo->largestBucketSize = (unsigned int)largestBucketSize;
    //Only run through UseFactor if it is not a tempptr
	return 0;
}

int SetResizeBehaviour( HashTablePTR hashTable, int dynamicBehaviour, float expandUseFactor, float contractUseFactor )
{
	(hashTable->hashTableInfo)->dynamicBehaviour = dynamicBehaviour;
	(hashTable->hashTableInfo)->expandUseFactor = expandUseFactor;
	(hashTable->hashTableInfo)->contractUseFactor = contractUseFactor;
	return 0;
}

////////////////////////////////////////////////////////////////////////////

treeNode * NewTreeNode(char *key, void *data)
{
	treeNode * newNode = malloc(sizeof(treeNode));
	newNode->key = malloc(sizeof(key));
	strcpy(newNode->key, key);
	newNode->value = (char *)data;
	newNode->left = NULL;
	newNode->right = NULL;
	return newNode;
}

void InsertNode(treeNode **root, char *key, void *data, void **existingDataHandle, HashTablePTR hashTable, int *outcome)
{
	if( (*root) == NULL)
	{
		*root =	NewTreeNode(key, data);
		*existingDataHandle = (*root)->key;
		hashTable->numEntries ++;
		(*outcome) = 1;	//Insertion with no collisions
	}
	else if( strcmp((*root)->key, key) == 0)
	{
		fprintf(stdout, "'%s' now contains '%s'.\n", (*root)->key, data);
		*existingDataHandle = (*root)->value;
		(*root)->value = (char *)data;
		(*outcome) = 2; //Replacement is done
	}
	else if( strcmp((*root)->key, key) > 0)
		InsertNode( &((*root)->left), key, data, existingDataHandle, hashTable, outcome);
	else if( strcmp((*root)->key, key) < 0)
		InsertNode( &((*root)->right), key, data, existingDataHandle, hashTable, outcome);
}

	
void ReallocateTable(HashTablePTR hashTable, treeNode * root)
{
	if(root != NULL)
	{
		ReallocateTable(hashTable, root->left);
		ReallocateTable(hashTable, root->right);
		
		char * key = malloc(81 * sizeof(char));
		char * value = malloc(81 * sizeof(char));
		strcpy(key, root->key);
		strcpy(value, root->value);
		char * existingData = NULL;
		InsertEntry(hashTable, key, value, (void**) &existingData);
		free(key);
	}
}

int InsertEntry( HashTablePTR hashTable, char *key, void *data, void **existingDataHandle )
{	
	if(hashTable->sentinel != (int)0xDEADBEEF)
		return -1;
	
	//Determine the correct bucket to enter
	int hashValue = SimpleIntHash(key, hashTable->numBuckets);
	int outcome = 0; //0 if inserted into blank, 1 if hash collision, 2 for replacement
	const int previousNumEntries = hashTable->numEntries; //Determine if replacement was done
	InsertNode((hashTable->arraybucketPTR + hashValue), key, data, existingDataHandle, hashTable, &outcome);
	
	if( ((*(hashTable->arraybucketPTR + hashValue))->left == NULL) && ((*(hashTable->arraybucketPTR + hashValue))->right == NULL) && (previousNumEntries != hashTable->numEntries))
		outcome = 0;
		
	GetHashTableInfo(hashTable, hashTable->hashTableInfo); //Update the HashTableInfo
	if((hashTable->hashTableInfo)->dynamicBehaviour == 1)
	{
		if(hashTable->numEntries < 2 && hashTable->numBuckets == 1)
			return outcome;
		if( (float)(hashTable->hashTableInfo)->useFactor > (hashTable->hashTableInfo)->contractUseFactor && ((float)(hashTable->hashTableInfo)->useFactor < (hashTable->hashTableInfo)->expandUseFactor) )
			return outcome;
		
		(hashTable->hashTableInfo)->bucketCount = (unsigned int)hashTable->numBuckets;
		(hashTable->hashTableInfo)->loadFactor = (float)(hashTable->numEntries)/(hashTable->numBuckets);
		
		UseFactor(&hashTable);
		HashTableObject *tempHashTable;
		//If use factor is too small, take away a bucket
		if( (hashTable->hashTableInfo)->useFactor < (hashTable->hashTableInfo)->contractUseFactor )
		{
			CreateHashTable(&tempHashTable, (unsigned int)(hashTable->numBuckets - 1));
			fprintf(stdout, "Due to dynamic allocation, the number of buckets has been decreased to %d!\n", tempHashTable->numBuckets);
		}
		//If use factor is too large, add a bucket
		else if( (float)(hashTable->hashTableInfo)->useFactor > (hashTable->hashTableInfo)->expandUseFactor)
		{
			CreateHashTable(&tempHashTable, (unsigned int)(hashTable->numBuckets + 1));
			fprintf(stdout, "Due to dynamic allocation, the number of buckets has been increased to %d!\n", tempHashTable->numBuckets);
		}
		
		for(int i = 0; i < hashTable->numBuckets; i++)
		{
			ReallocateTable(tempHashTable, *(hashTable->arraybucketPTR + i));
		}
		
		DestroyHashTable(&hashTable);
		hashTable = tempHashTable;
	}
	return 0;
}
	
//////////////////////////////////////////////////////////////////////////////

treeNode *FindItem(treeNode * root, char * key)
{
	if(root != NULL)
	{
		if(strcmp(root->key, key) > 0)
			return FindItem(root->left, key);
		else if(strcmp(root->key, key) < 0)
			return FindItem(root->right, key);
		else if(strcmp(root->key, key) == 0)
			return root;
	}
	return NULL;
}

int FindEntry( HashTablePTR hashTable, char *key, void **data )
{
	int hashValue = SimpleIntHash(key, hashTable->numBuckets);
	struct buckets * tempptr = *((hashTable->arraybucketPTR) + hashValue);
	
	//No Hash Collision
	if(tempptr != NULL)
	{
		treeNode * found = NULL;
		found = FindItem(*(hashTable->arraybucketPTR + hashValue), key);
		if(found == NULL)
			return -1;
		*data = found->value;
		return 0;
	}
	return 0;
}

//////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////

void StoreKeys( treeNode *root, char ***keysArrayHandle, int * count )
{
	if(root != NULL)
	{
		StoreKeys(root->left, keysArrayHandle, count);
		StoreKeys(root->right, keysArrayHandle, count);
		*( *keysArrayHandle + *count) = root->key;
		(*count) ++;
	}
}

void StoreValues( treeNode *root, char ***keysArrayHandle, int * count )
{
	if(root != NULL)
	{
		StoreKeys(root->left, keysArrayHandle, count);
		StoreKeys(root->right, keysArrayHandle, count);
		*( *keysArrayHandle + *count) = root->value;
		(*count) ++;
	}
}

int GetKeys( HashTablePTR hashTable, char ***keysArrayHandle, unsigned int *keyCount )
{
	//Create an array of pointers with the length of the array being the num_entries.
	*keysArrayHandle = malloc(sizeof(char *)*(unsigned long)(hashTable->numEntries));
	for(int i = 0; i < hashTable->numEntries; i++)
		*(*keysArrayHandle + i) = NULL;
		
	int count = 0;
	for(int i = 0; i < hashTable->numBuckets; i++)	//Loop through the array of struct bucket pointers.
	{
		struct buckets *tempptr = *(hashTable->arraybucketPTR + i);
		if(tempptr == NULL) //If current bucket is empty, move on to the next
			continue;
		else
			StoreKeys( tempptr, keysArrayHandle, &count);
	}
	*keyCount = (unsigned int)hashTable->numEntries;
	return 0;
}

//////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////

char * findSmallest(treeNode *root)
{
    if(root->left != NULL)
    {
        return findSmallest(root->left);
    }
    else
    {
        return root->key;
    }
}

int DeleteNode(treeNode ** root, char * key, void **data)
{
    if (*root != NULL)
    {
        if(strcmp((*root)->key, key) > 0)
        {
            return DeleteNode(&((*root)->left), key, data);
        }
        else if(strcmp((*root)->key, key) > 0)
        {
            return DeleteNode(&((*root)->right), key, data);
        }
        else
        {
            treeNode * delPTR = *root;

            if((*root)->left == NULL && (*root)->right == NULL)
            {
				*data = (*root)->value;
                free(delPTR);
                *root = NULL;
            }
            else if((*root)->left == NULL && (*root)->right != NULL)
            {
				*data = (*root)->value;
                *root = (*root)->right;
                free(delPTR);
            }
            else if((*root)->left != NULL && (*root)->right == NULL)
            {
				*data = (*root)->value;
                *root = (*root)->left;
                free(delPTR);
            }
            else
            {
                char * smallestRight = findSmallest(*root);
                DeleteNode(root, smallestRight, data);
                (*root)->key = smallestRight;
            }

            return 0;
        }
    }
    else{return -1;}
}

int DeleteEntry( HashTablePTR hashTable, char *key, void **data )
{
	int hashValue = SimpleIntHash(key, hashTable->numBuckets);
	DeleteNode( ((hashTable->arraybucketPTR) + hashValue), key, data);
	return 0;
}	
