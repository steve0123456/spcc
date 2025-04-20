%{
#include <stdio.h>
#include <stdlib.h>

int a_count = 0;
int b_count = 0;
int c_count = 0;

void yyerror(const char *s);
int yylex(void);
%}

%token a b c NL

%%
Input : Sequence NL {
    if (a_count == b_count && b_count == c_count)
        printf("✅ Valid string\nCounts -> a: %d, b: %d, c: %d\n", a_count, b_count, c_count);
    else
        printf("❌ Invalid string\nCounts -> a: %d, b: %d, c: %d\n", a_count, b_count, c_count);
    exit(0);
};

Sequence : A B C;

A : A a { a_count++; }
  | /* empty */ ;

B : B b { b_count++; }
  | /* empty */ ;

C : C c { c_count++; }
  | /* empty */ ;
%%

int main() {
    printf("Enter a string of the form aⁿbⁿcⁿ:\n");
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    printf("❌ Syntax Error: %s\n", s);
    exit(1);
}
