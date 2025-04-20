#ifndef SERIES

#define fact(n){                \
    int fact = 1;               \
    if((n) == 0){               \
        return fact;            \
    }                           \
    for(int i=1;i<=(n);i++)      \
    {                           \
        fact = fact * i;        \
    }                           \
    printf("%d \n",fact);        \
}

#define prime(n)                                     \
    {                                                \
        printf("Prime Numbers up to %d:\n", (n));    \
        for (int i = 2; i <= (n); i++) {             \
            int prime = 1;                           \
            for (int j = 2; j * j <= i; j++) {       \
                if (i % j == 0) {                    \
                    prime = 0;                       \
                    break;                           \
                }                                    \
            }                                        \
            if (prime)                               \
                printf("%d ", i);                    \
        }                                            \
        printf("\n");                                \
    }

#define Leap(start, end)                                             \
    {                                                                \
        printf("Leap Years from %d to %d:\n", (start), (end));       \
        for (int year = (start); year <= (end); year++) {            \
            if ((year % 4 == 0 && year % 100 != 0) ||                \
                (year % 400 == 0))                                   \
                printf("%d ", year);                                 \
        }                                                            \
        printf("\n");                                                \
    }
#endif