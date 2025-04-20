%{
#include "demo.tab.h"
extern int a_count, b_count;
%}

%%
a   { return a; }
b   { return b; }
\n  { return NL; }
.   { return -1; } // invalid characters
%%
int yywrap() { return 1; }
