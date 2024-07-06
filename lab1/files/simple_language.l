%{
#include <cstdlib>
#include <string>
#include "y.tab.h"

%}

%%

[a-zA-Z][a-zA-Z0-9]*    { yylval.str = new std::string(yytext);  return VARIABLE; }
[0-9]+                  { yylval.num = strtol(yytext, NULL, 10); return NUMBER; }
[()=+\-*/^;.]           { return *yytext; }
"\n"                    { return '\n'; }
[\t]                   ;  
" "+                    ;
.                       { printf("Unknown character: %c\n", *yytext); }

%%

int yywrap() {
    return 1;
}

