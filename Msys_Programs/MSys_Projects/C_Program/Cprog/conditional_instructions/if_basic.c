// C Program to check whether a nummber is even or odd
#include<stdio.h>

int main(){
    int a, b;
    printf("Enter a number\n");
    scanf("%d",&a);

    if(a%2==0){
        printf("%d is a even", a);
    }    
    else{
        printf("%d is a odd",a);
    }
    return 0;
}