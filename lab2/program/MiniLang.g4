grammar MiniLang;

prog: stat+;

stat:
    'print' '(' expr ')' ';'    # printExpr
    | functionDecl              # funcDecl
    | assignment ';'            # assign
    | ifBlock                   # ifStat
    | whileBlock                # whileStat
    | returnStatement ';'       # returnStat
    | NEWLINE                   # blank;

ifBlock: 'if' expr block ('else' block)?;

whileBlock: 'while' expr 'do' block;

block: '{' stat* '}';

assignment: ID '=' expr;

expr:
    constant                    # constantExpr
    | expr ('*' | '/') expr     # MulDiv
    | expr ('+' | '-') expr     # AddSub
    | ID                        # id
    | '(' expr ')'              # parens
    | expr compareOp expr       # compare
    | functionCall              # funcCall;

compareOp: '==' | '!=' | '<' | '<=' | '>' | '>=';

constant: INT | STRING | BOOLEAN | FLOAT | NULL;

MUL: '*'; 
DIV: '/'; 
ADD: '+'; 
SUB: '-'; 
ID: [a-zA-Z]+; 

INT: [0-9]+; 
STRING: '"' (~["])* '"'; 
BOOLEAN: 'true' | 'false'; 
FLOAT: [0-9]+ '.' [0-9]+; 
NULL: 'null'; 

NEWLINE: '\r'? '\n'; 
COMMENT: '//' ~[\r\n]* -> skip; 
WS: [ \t]+ -> skip; 

EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';

FUNC: 'func';
RETURN: 'return';

functionDecl
    : FUNC ID '(' (param (',' param)*)? ')' block
    ;

param
    : ID
    ;

functionCall
    : ID '(' (expr (',' expr)*)? ')'
    ;

returnStatement
    : RETURN expr
    ;

comparisonExpr
    : expression EQ expression
    | expression NEQ expression
    | expression LT expression
    | expression GT expression
    | expression LTE expression
    | expression GTE expression
    ;

expression
    : comparisonExpr
    | functionCall
    ;
