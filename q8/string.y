%{
#include<stdio.h>
#include<stdlib.h>
void yyerror();
int yylex();
%}
%token a b NL
%%
Statement: S NL { printf("Valid String\n"); exit(0); };
S: a A b;
A: A a | ;
%%

void main()
{
printf("\nEnter String: ");
yyparse();
}
void yyerror()
{
printf("Invalid String");
exit(0);
}