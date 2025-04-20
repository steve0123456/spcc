%{
#include <stdio.h>
%}

%%
^[6-9][0-9]{9}$    { printf("✅ Valid Mobile Number: %s\n", yytext); }
[0-9]+             { printf("❌ Invalid Mobile Number: %s\n", yytext); }
.|\n               { /* ignore other characters */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a 10-digit mobile number (starting with 6-9):\n");
    yylex();
    return 0;
}
