%{
#include <stdio.h>
%}

%%
[0-9]+ {
    int len = strlen(yytext);
    char last = yytext[len - 1];
    if (last == '0' || last == '2' || last == '4' || last == '6' || last == '8')
        printf("✅ %s is EVEN\n", yytext);
    else
        printf("🔹 %s is ODD\n", yytext);
}

.|\n   { /* ignore non-numeric inputs */ }

%%

int yywrap() { return 1; }

int main() {
    printf("Enter a number to check even or odd (Ctrl+D to end on Linux / Ctrl+Z on Windows):\n");
    yylex();
    return 0;
}
