%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *);
int yylex();

int a_count = 0;
int b_count = 0;
%}

%token a b NL

%%
Statement : S NL {
    if (a_count % 2 == 0 && b_count == a_count / 2)
        printf("✅ Valid String\na = %d, b = %d\n", a_count, b_count);
    else
        printf("❌ Invalid String\na = %d, b = %d\n", a_count, b_count);
    exit(0);
};

S : A B;

A : A a { a_count++; }
  | /* empty */;

B : B b { b_count++; }
  | /* empty */;
%%

int main() {
    printf("Enter string (form: a^(2n) b^n):\n");
    yyparse();
    return 0;
}

void yyerror(const char *msg) {
    printf("❌ Invalid String: %s\n", msg);
    exit(0);
}
