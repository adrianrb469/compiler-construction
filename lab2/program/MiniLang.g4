grammar MiniLang;

prog: stat+;

stat:
	'print' '(' expr ')' ';'	# printExpr
	| assignment ';'			# assign
	| ifBlock					# ifStat
	| whileBlock				# whileStat
	| NEWLINE					# blank
	| INVALID_CHAR				# unrecognizedToken;

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
	| expr compareOp expr	# compare
	| functionCall			# funcCall;

compareOp: '==' | '!=' | '<' | '<=' | '>' | '>=';

constant: INT | STRING | BOOLEAN | FLOAT | NULL;

// types
INT: [0-9]+; // match integers
FLOAT: [0-9]+ '.' [0-9]+; // match floats
STRING: ('"' ~'"'* '"'); // basically, anything between double quotes that isn't a double quote
BOOLEAN: 'true' | 'false'; // match booleans
NULL: 'null'; // match null 

MUL: '*'; // define token for multiplication
DIV: '/'; // define token for division
ADD: '+'; // define token for addition
SUB: '-'; // define token for subtraction
ID: [a-zA-Z]+; // match identifiers

NEWLINE:
	'\r'? '\n'; // return newlines to parser (is end-statement signal)
COMMENT: '//' ~[\r\n]* -> skip; // match inline comments

EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';

FUNC: 'func';
RETURN: 'return';

functionDecl: FUNC ID '(' (param (',' param)*)? ')' block;

param: ID;

functionCall: ID '(' (expr (',' expr)*)? ')';

returnStatement: RETURN expr;

comparisonExpr:
	expression EQ expression
	| expression NEQ expression
	| expression LT expression
	| expression GT expression
	| expression LTE expression
	| expression GTE expression;

expression: comparisonExpr | functionCall;
INVALID_CHAR: .;
