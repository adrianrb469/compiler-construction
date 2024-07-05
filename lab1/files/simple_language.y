%{
#include <iostream>
#include <string>
#include <map>

static std::map<std::string, int> vars;

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
%token<str> ID
%type<num> expression
%type<num> assignment

%right '='
%left '+' '-'
%left '*' '/'

%%

program: statement_list
        ;

statement_list: statement
    | statement_list statement
    ;

statement: assignment
    | expression ':' { std::cout << "Result: " << $1 << std::endl; }
    | error { yyerror("Syntax error in statement. Please check your input."); yyclearin; }
    ;

assignment: ID '=' expression
        { vars[*$1] = $3; delete $1; std::cout << "Assigned " << *$1 << " = " << $3 << std::endl; }
    ;

expression: NUMBER { $$ = $1; }
    | ID { 
        if (vars.find(*$1) == vars.end()) {
            // if variable not found, return 0
            yyerror("Undefined variable.");
            $$ = 0;
            return 0;`
        }
        $$ = vars[*$1]; 
        delete $1;  
        std::cout << "Value of " << *$1 << " = " << $1 << std::endl;
    }
    | ID '=' expression { vars[*$1] = $3; delete $1; $$ = $3; }
    | expression '+' expression { $$ = $1 + $3; }
    | expression '-' expression { $$ = $1 - $3; }
    | expression '*' expression { $$ = $1 * $3; }
    | expression '/' expression { 
        if ($3 == 0) {
            yyerror("Division by zero is not allowed.");
            $$ = 0;
        } else {
            $$ = $1 / $3;
        }
    }
    | error { yyerror("Syntax error in expression. Please check your input."); yyclearin; }
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
