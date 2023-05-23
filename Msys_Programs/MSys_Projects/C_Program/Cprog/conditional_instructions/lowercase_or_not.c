#include<stdio.h>

int main(){
    // 97-122 = a-z characters ASCII values
    char ch;
    printf("Enter your characters: ");
    scanf("%c",&ch);
    if(ch<=122 && ch>=97){
        printf("It is lowercase");
    }
    else{
        printf("It is uppercase");
    }
    return 0;
}