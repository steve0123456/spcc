%{
#include "abc.tab.h"
%}

%%
a     { return a; }
b     { return b; }
c     { return c; }
\n    { return NL; }
.     { return -1; } // any invalid char
%%
int yywrap() { return 1; }
