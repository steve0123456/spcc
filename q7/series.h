#ifndef SERIES

#define fib(n) do {                                      \
    int a = 0, b = 1, temp;                              \
    printf("Fibonacci: %d\t", a);                        \
    for (int i = 1; i < (n); i++) {                      \
        printf("%d\t", b);                               \
        temp = a + b;                                    \
        a = b;                                           \
        b = temp;                                        \
    }                                                    \
    printf("\n");                                        \
} while(0)

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