#ifndef PROP_H
#define PROP_H

#include <stdio.h>

// Macro for factorial
#define FACTO(n) do {                                \
    int fact = 1;                                     \
    for (int i = 1; i <= (n); i++)                    \
        fact *= i;                                    \
    printf("Factorial of %d is %d\n", (n), fact);     \
} while (0)

// Macro for sum of natural numbers
#define SUMNO(n) do {                                 \
    int s = (n) * ((n) + 1) / 2;                      \
    printf("Sum of natural numbers till %d is %d\n",  \
           (n), s);                                   \
} while (0)

#endif
