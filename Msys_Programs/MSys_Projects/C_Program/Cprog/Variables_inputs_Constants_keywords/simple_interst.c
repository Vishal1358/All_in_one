#include<stdio.h>

int main(){
    int principle=200000, rate=4, year=2;
    int simpleInterst = (principle*rate*year)/100;
    printf("The value of simple interst is %d", simpleInterst);
    return 0;
}