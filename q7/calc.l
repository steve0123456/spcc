%{
#include<stdio.h>
#include "string.tab.h"
%}
%%
[a] {return a;}
[b] {return b;}
\n {return NL;}
. {return yytext[0];}
%%
int yywrap()
{
return 1;
}