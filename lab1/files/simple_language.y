%{
#include <iostream>
#include <map>
#include <string>
#include <cmath>

std::map<std::string, int> vars;

inline void yyerror(const char *str) { 
    std::cerr << "Error: " << str << std::endl; 
    // Clear the input buffer in case of error
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int yylex();
%}

%union { int num; std::string *str; }

%token<num> NUMBER
%token<str> VARIABLE
%type<num> expression
%type<num> assignment statement

%right '='
%left '+' '-'
%left '*' '/'
%left '^'

%%

program: program statement '\n'
    | 
    ;

statement: 
    expression { printf("%d\n", $1); }
    | assignment
    ;

assignment:
    VARIABLE '=' expression { vars[*$1] = $3; printf("Assigned %d to %s\n", $3, $1->c_str()); }
    | VARIABLE '=' { yyerror("Empty assignment is not allowed."); }
    ;

expression: 
    NUMBER 
    | VARIABLE  { 
        if (vars.find(*$1) == vars.end()) {
            yyerror(("Variable '" + *$1 + "' is not assigned anything.").c_str());
            $$ = 0; // Or handle as you see fit
        } else {
            $$ = vars[*$1];
        }
    }
    | expression '+' expression { $$ = $1 + $3; }
    | expression '-' expression { $$ = $1 - $3; }
    | expression '*' expression { $$ = $1 * $3; }
    | expression '^' expression { $$ = pow($1, $3); }
    | expression '/' expression { 
        if ($3 == 0) {
            yyerror("Division by zero is not allowed.");
            $$ = 0; // Or handle as you see fit
        } else {
            $$ = $1 / $3;
        }
    }
    | '(' expression ')' { $$ = $2; }
    ;

%%

extern int yylex();
extern int yyparse();

int main() {
    while (true) {
        yyparse();
    }
    return 0;
}
