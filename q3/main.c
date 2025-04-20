#include <stdio.h>
#include "conv.h"

int main()
{   
    int ch;
    double x;
    
    do{
        printf("enter the choice : 0.exit\n 1.feet to convert to metres:\n   2.metres to convert to feet\n  3.litres to convert to cubic feet:\n  4.cubic feet to convert to litres:\n  5.Celsius to convert to Fahrenheit:\n   6.Fahrenheit to convert to Celsius:");
        scanf("%d",&ch);

        switch (ch)
        {
        case 0:
            printf("exiting");
            break;

        case 1:
            printf("enter value");
            scanf("%lf",&x);
            printf("value : %lf \n",f_to_m(x));
            break;

        case 2:
            printf("enter value");
            scanf("%lf",&x);
            printf("value : %lf \n",m_to_f(x));
            break;

        case 3:
            printf("enter value");
            scanf("%lf",&x);
            printf("value : %lf \n",l_to_cf(x));
            break;

        case 4:
            printf("enter value");
            scanf("%lf",&x);
            printf("value : %lf \n",cf_to_l(x));
            break;

        case 5:
            printf("enter value");
            scanf("%lf",&x);
            printf("value : %lf \n",cel_to_far(x));
            break;

        case 6:
            printf("enter value");
            scanf("%lf",&x);
            printf("value : %lf \n",far_to_cel(x));
            break;
        
        default:
            printf("enter valid choice");
            break;
        }

    }while(ch != 0);

    return 0;
}