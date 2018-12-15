#include <stdio.h>
#include <stdlib.h>

//capacity,top,array
struct Stack
{
    int top;
    int* array;
    unsigned capacity;
};

//create stack : capacity (top,array)
struct Stack* createStack(unsigned capacity)
{
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->top=-1;
    stack->capacity=capacity;
    stack->array = (int*)malloc(sizeof(int)*capacity);
    return stack;
}


//is full top == capacity
int isFull(struct Stack* stack)
{
    return(stack->capacity-1==stack->top);
}

//is empty top =-1
int isEmpty(struct Stack* stack)
{
    return(-1==stack->top);
}

//top
int top(struct Stack* stack)
{
    return(stack->top);
}

//push -> stack,item
//check if full
//top+1

void push(struct Stack* stack,int item)
{
    if (isFull(stack))
        return;
    printf("%d ->> pushed in Stack\n",item);
    stack->top+=1;
    stack->array[stack->top]=item;



}

//pop

void pop(struct Stack* stack)
{
    if (isEmpty(stack))
        return;
    int item=top(stack);
    printf("%d <<-- poped in Stack\n",item);
    stack->top-=1;
}

int main()
{
    struct Stack* stack = createStack(1000);
    push(stack,10);
    push(stack,100);
    push(stack,10);
    pop(stack);


}


    



