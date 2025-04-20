%{
#include <stdio.h>

int u_count = 0, l_count = 0;
%}

%%

[A-Z]     { u_count++; }
[a-z]     { l_count++; }

%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter text: ");
    yylex();
    printf("\nUppercase count: %d\n", u_count);
    printf("Lowercase count: %d\n", l_count);
    return 0;
}
