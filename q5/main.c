// main.c

#include <stdio.h>
#include <stdlib.h>
#include "conv.h"

int main() {
    int choice, decimal;
    char binary[100], hex[100];

    while (1) {
        printf("\n==== Conversion Menu ====\n");
        printf("1. Binary to Decimal\n");
        printf("2. Decimal to Binary\n");
        printf("3. Binary to Hexadecimal\n");
        printf("4. Hexadecimal to Binary\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter binary number: ");
                scanf("%s", binary);
                printf("Decimal: %d\n", BINARY_TO_DECIMAL(binary));
                break;

            case 2:
                printf("Enter decimal number: ");
                scanf("%d", &decimal);
                DECIMAL_TO_BINARY(decimal);
                break;

            case 3:
                printf("Enter binary number: ");
                scanf("%s", binary);
                BINARY_TO_HEX(binary);
                break;

            case 4:
                printf("Enter hexadecimal number: ");
                scanf("%s", hex);
                HEX_TO_BINARY(hex);
                break;

            case 5:
                printf("Exiting program.\n");
                exit(0);

            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}
