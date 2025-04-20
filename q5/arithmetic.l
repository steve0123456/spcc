%{
#include <stdio.h>
int valid = 1;  // Will be set to 0 if any invalid token is found
%}

%%


[ \t\n]+                ;

[0-9]+                  { printf("Number: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*  { printf("Identifier: %s\n", yytext); }

[\+\-\*/=]              { printf("Operator: %s\n", yytext); }

[(|)]                   { printf("Parenthesis: %s\n", yytext); }

.                       { 
                          printf("Invalid token: %s\n", yytext); 
                          valid = 0;
                        }

%%

int yywrap() { return 1; }

int main() {
    printf("Enter an arithmetic expression:\n");
    yylex();
    
    if (valid)
        printf("\nExpression is VALID.\n");
    else
        printf("\nExpression is INVALID.\n");
    
    return 0;
}
