%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *);
int yylex();

int i = 0;
int j = 0;
%}

%token a b NL

%%
Statement : S NL {
    if (i + 1 == j)
        printf("✅ Valid String\na = %d, b = %d\n", i, j);
    else
        printf("❌ Invalid String\na = %d, b = %d\n", i, j);
    exit(0);
};

S : A B;

A : A a { i++; }
  | /* empty */;

B : B b { j++; }
  | /* empty */;
%%

int main() {
    printf("Enter string (a^n b^(n+1)) followed by Enter:\n");
    yyparse();
    return 0;
}

void yyerror(const char *msg) {
    printf("❌ Invalid String: %s\n", msg);
    exit(0);
}
