#include <stdio.h>
#include "series.h"

int main(){
    double x,n,start,end;

    printf("enter no for factorial");
    scanf("%lf",&x);

    printf("enter no for prime");
    scanf("%lf",&n);

    printf("enter years start to end");
    scanf("%lf %lf",&start,&end);

    fact(x);
    prime(n);
    Leap(start,end);

    return 0;
}