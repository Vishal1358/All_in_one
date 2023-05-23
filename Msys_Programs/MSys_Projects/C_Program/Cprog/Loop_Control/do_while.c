#include<stdio.h>

int main(){
    // int i = 220;
    int i = 1;

    //do_while ---> executes the code and then checks the condition
    do
    {
        printf("The value of i is %d\n", i);
        i++;
    } while (i<=10);
    
    return 0;
}