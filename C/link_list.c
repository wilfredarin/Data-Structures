/*
how to run
gcc -o hello hello.c
executable file first hello is name of the exrercutable
./hello
executable file

ptr = (cast-type*) malloc(byte-size)
malloc function rturns a pointer to an area of memory 

x->field == (*x).field
x->field---------field attribute of value at x
accountp->account_number; == (*accountp).account_number;



*/

#include <stdio.h>
#include <stdlib.h>


struct Node
{

	int data;
	struct Node *next;

};

int main()
{
	struct Node* head = NULL; // struct node tyoe ka variable create kara,,,, clled head and intialised it to none
	struct Node* second = NULL;
	struct Node* third = NULL;

	head = (struct Node*)malloc(sizeof(struct Node)); // head is a pointer variable which point to a memory area 
	second = (struct Node*)malloc(sizeof(struct Node));
	third = (struct Node*)malloc(sizeof(struct Node));
		
	head->data = 1; 		//(*head).data = 1 so we are assigning value to data atribute of (value which is stored at head)

						   //assign data in first node
    head->next = second;  // Link first node with 
                         // the second node
   
    second->data = 2; 
 
  // Link second node with the third node
    second->next = third;
   
   third->data = 3; //assign data to third node
   third->next = NULL;
   
   printf("%d da\n",head->data );


  return 0;
}


	

