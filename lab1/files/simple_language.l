%{
#include <cstdlib>
#include <string>
#include "y.tab.h"
%}

%%

[a-zA-Z][a-zA-Z0-9]*    { yylval.str = new std::string(yytext);  return VARIABLE; }
[0-9]+                  { yylval.num = strtol(yytext, NULL, 10); return NUMBER; }
[()=+*/^;.]             { return *yytext; }
"\n"                    { return '\n'; }
[ \t]                   ;  // skip whitespace
.                       ; /* ignore all the rest */
%%

int yywrap() {
    return 1;
}
