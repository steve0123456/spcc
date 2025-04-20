#include <stdio.h>
#include "geometry.h"

/*
gcc main.c -o geometry_program
./geometry_program
*/

int main()
{
    double radius,length,breadth,side,base,height;

    printf("enter radius");
    scanf("%lf",&radius);

    printf("enter length and breadth");
    scanf("%lf %lf",&length,&breadth);

    printf("enter side");
    scanf("%lf",&side);

    printf("enter base and height");
    scanf("%lf %lf",&base,&height);

    printf("\n--- Area Results ---\n");
    printf("Area of Circle: %.2f\n", area_circle(radius));
    printf("Area of Rectangle: %.2f\n", area_rect(length, breadth));
    printf("Area of Square: %.2f\n", area_square(side));
    printf("Area of Triangle: %.2f\n", area_tri(base, height));

    return 0;

}

