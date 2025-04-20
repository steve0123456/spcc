%{

#include<stdio.h>

int v_count =0,c_count =0;

%}

%%

[aeiouAEIOU] {v_count++;}
[b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z] {c_count++;}

.|\n

%%

int yywrap() {return 1;}

int main(){
    printf("enter text");
    yylex();
    printf("vowels are %d",v_count);
    printf("consonant are %d",c_count);
    return 0;
}