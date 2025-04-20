%{
#include <stdio.h>
#include <string.h>

int keyword_count = 0, id_count = 0, number_count = 0, op_count = 0, punct_count = 0;

// List of C-like keywords
char *keywords[] = { "if", "else", "while", "for", "return", "int", "float", "char", "void", "break", "continue" };
int is_keyword(char *word) {
    for (int i = 0; i < sizeof(keywords)/sizeof(keywords[0]); i++) {
        if (strcmp(word, keywords[i]) == 0)
            return 1;
    }
    return 0;
}
%}

%%

[ \t\n]+            ;  // ignore spaces, tabs, newlines

[a-zA-Z_][a-zA-Z0-9_]*  {
                        if (is_keyword(yytext)) {
                            keyword_count++;
                            printf("Keyword: %s\n", yytext);
                        } else {
                            id_count++;
                            printf("Identifier: %s\n", yytext);
                        }
                      }

[0-9]+              {
                        number_count++;
                        printf("Number: %s\n", yytext);
                   }

[+\-*/=<>]          {
                        op_count++;
                        printf("Operator: %s\n", yytext);
                   }

[;:,(){}]           {
                        punct_count++;
                        printf("Punctuation: %s\n", yytext);
                   }

.                   { printf("Unknown token: %s\n", yytext); }

%%

int yywrap() { return 1; }

int main() {
    printf("Enter your code snippet:\n");
    yylex();
    printf("\n--- Token Summary ---\n");
    printf("Keywords: %d\n", keyword_count);
    printf("Identifiers: %d\n", id_count);
    printf("Numbers: %d\n", number_count);
    printf("Operators: %d\n", op_count);
    printf("Punctuation: %d\n", punct_count);
    return 0;
}
