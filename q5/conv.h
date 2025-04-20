// conversion.h

#ifndef CONV
#define CONV

#include <stdio.h>
#include <math.h>
#include <string.h>

// Macro to convert binary to decimal
#define BINARY_TO_DECIMAL(binStr) ({                      \
    int dec = 0;                                           \
    for (int i = 0; binStr[i] != '\0'; i++) {             \
        dec = dec * 2 + (binStr[i] - '0');                \
    }                                                     \
    dec;                                                  \
})

// Macro to convert decimal to binary (prints directly)
#define DECIMAL_TO_BINARY(num) ({                         \
    printf("Binary: ");                                   \
    int n = num;                                          \
    int bin[32], i = 0;                                   \
    if (n == 0) printf("0");                              \
    else {                                                \
        while (n > 0) {                                   \
            bin[i++] = n % 2;                             \
            n /= 2;                                       \
        }                                                 \
        for (int j = i - 1; j >= 0; j--)                  \
            printf("%d", bin[j]);                         \
    }                                                     \
    printf("\n");                                         \
})

// Macro to convert binary to hexadecimal
#define BINARY_TO_HEX(binStr) ({                          \
    int dec = BINARY_TO_DECIMAL(binStr);                  \
    printf("Hexadecimal: %X\n", dec);                     \
})

// Macro to convert hexadecimal to binary (prints directly)
#define HEX_TO_BINARY(hexStr) ({                          \
    unsigned int x;                                       \
    sscanf(hexStr, "%x", &x);                             \
    printf("Binary: ");                                   \
    for (int i = 31, start = 0; i >= 0; i--) {            \
        int bit = (x >> i) & 1;                           \
        if (bit || start) {                               \
            printf("%d", bit);                            \
            start = 1;                                    \
        }                                                 \
    }                                                     \
    if (!x) printf("0");                                  \
    printf("\n");                                         \
})

#endif
