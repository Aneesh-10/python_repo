#include<stdio.h>
main()
{
	FILE *fp;
	char dataToBeRead[50];
	fp=fopen("123","r");
	//printf(fp);
	//fputs("\n",fp);
	while( fgets ( dataToBeRead, 50, fp ) != NULL ) 
        { 
          
            // Print the dataToBeRead  
            printf( "%s" , dataToBeRead ) ; 
         } 
	//fputs(data, fp);
	//fputs("\n",fp);
	fclose(fp);
}
