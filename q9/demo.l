%{
#include "demo.tab.h"
%}

%%
a   { return a; }
b   { return b; }
\n  { return NL; }
.   { return -1; } // Any invalid character
%%
int yywrap() { return 1; }
