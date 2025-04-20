%{
#include <stdio.h>

int line_count = 0;
int number_count = 0;
int space_count = 0;
%}

%%
[0-9]+      { number_count++; }
[ \t]       { space_count++; }
\n          { line_count++; }
.           { }  // Ignore other characters
%%

int yywrap() { return 1; }

int main() {
    printf("Enter text (Ctrl+D to end on Linux / Ctrl+Z on Windows):\n");
    yylex();

    printf("\n✅ Results:\n");
    printf("Lines       : %d\n", line_count);
    printf("Numbers     : %d\n", number_count);
    printf("Blank spaces: %d\n", space_count);

    return 0;
}
