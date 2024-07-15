grammar MiniLang;

prog: stat+;

stat:
	'print' '(' expr ')' ';'	# printExpr
	| assignment ';'			# assign
	| ifBlock					# ifStat
	| whileBlock				# whileStat
	| NEWLINE					# blank;

ifBlock: 'if' expr block ('else' block)?;

whileBlock: 'while' expr 'do' block;

block: '{' stat* '}';

assignment: ID '=' expr;

expr:
	constant				# constantExpr
	| expr ('*' | '/') expr	# MulDiv
	| expr ('+' | '-') expr	# AddSub
	| ID					# id
	| '(' expr ')'			# parens
	| expr compareOp expr	# compare;

compareOp: '==' | '!=' | '<' | '<=' | '>' | '>=';

constant: INT | STRING | BOOLEAN | FLOAT | NULL;

MUL: '*'; // define token for multiplication
DIV: '/'; // define token for division
ADD: '+'; // define token for addition
SUB: '-'; // define token for subtraction
ID: [a-zA-Z]+; // match identifiers

// types
INT: [0-9]+; // match integers
STRING: ('"' ~'"'* '"'); // basically, anything between double quotes that isn't a double quote
BOOLEAN: 'true' | 'false'; // match booleans
FLOAT: [0-9]+ '.' [0-9]+; // match floats
NULL: 'null'; // match null 

NEWLINE:
	'\r'? '\n'; // return newlines to parser (is end-statement signal)
COMMENT: '//' ~[\r\n]* -> skip; // match inline comments

WS: [ \t]+ -> skip; // toss out whitespace

EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';

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
    ;

INVALID_CHAR:
	.; // match any single character that is not in the grammar
