#include <stdio.h>
#include "series.h"

int main(){
    int n,x,start,end;
    
    printf("enter no for fibonnaci");
    scanf("%d",&n);

    printf("enter for prime");
    scanf("%d",&x);

    printf("enter year for start and end");
    scanf("%d %d",&start,&end);

    fib(n);
    prime(x);
    Leap(start,end);

    return 0;
}