#include<stdio.h>

int main(){
    int length, breadth;
    printf("What is your length of rectangle\n");
    scanf("%d", &length);
    printf("What is your breadth of rectangle\n");
    scanf("%d", &breadth);

    printf("The area of rectangle is %d", length*breadth);

    return 0;
}