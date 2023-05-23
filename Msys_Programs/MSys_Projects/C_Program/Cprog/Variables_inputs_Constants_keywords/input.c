#include<stdio.h>

int main()
{
    int a, b;
    printf("Enter the value of a\n");
    scanf("%d", &a); 
    // in order to take input from user use to scanf 
    // & is the address of operator  
    printf("Enter the value of a\n");   
    scanf("%d", &b);
    printf("The sum of a and b is %d", a+b);
    return 0;
}