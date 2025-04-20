%{
#include<stdio.h>
#include<string.h>
int sentence = 0;
int tabs = 0;
int spaces = 0;
int characters = 0;
int words = 0;
%}
%%
"END" {printf("\nSentences: %d \nCharacters: %d \nWords: %d \nTabs: %d \nSpaces: %d\n",
sentence,characters, words, tabs, spaces);}
"\n" {sentence++;}
" " {spaces++;}
"\t" {tabs++;}
[a-zA-Z0-9]* {words++; characters+= yyleng;}
%%
int yywrap(void){}
int main()
{
yylex();
return 0;
}