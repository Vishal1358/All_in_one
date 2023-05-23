#include<stdio.h>

int main(){
    int i=0, n, factrial=1;
    printf("Enter the number");
    scanf("%d",&n);
    for(i=1; i<=n; i++){
        factrial*=i;
    }
    printf("The value of factorial %d is %d", n, factrial);
    return 0;
}