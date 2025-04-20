%{
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int uppercase_token_count = 0;

// Function to check if token has uppercase letter
int has_uppercase(const char *str) {
    for (int i = 0; str[i]; i++) {
        if (isupper(str[i]))
            return 1;
    }
    return 0;
}
%}

%%

[[:alnum:]]+ {
    if (has_uppercase(yytext)) {
        uppercase_token_count++;
    }
}

.|\n    { /* Ignore all other characters */ }

%%

int yywrap() { return 1; }

int main() {
    printf("Enter input text (Ctrl+D to end on Linux / Ctrl+Z on Windows):\n");
    yylex();
    printf("\n✅ Number of tokens with uppercase letters: %d\n", uppercase_token_count);
    return 0;
}
