#include <stdio.h>

int main()
{
    int a;
    printf("Enter your age\n");
    scanf("%d", &a);
    if (a >= 18)
    {
        printf("Provide the driving liceance");
    }
    else
    {
        printf("You are below 18 age");
    }
    return 0;
}