grammar Compiscript;

program: declaration* EOF;

declaration: classDecl | funDecl | varDecl | statement;

classDecl:
	'class' IDENTIFIER ('extends' IDENTIFIER)? '{' methods '}';
funDecl: 'fun' function;
varDecl: 'var' IDENTIFIER ('=' expression)? ';';

statement:
	exprStmt
	| forStmt
	| ifStmt
	| printStmt
	| returnStmt
	| whileStmt
	| breakStmt
	| continueStmt
	| block;

breakStmt: 'break' ';';
continueStmt: 'continue' ';';

exprStmt: expression ';';
forStmt:
	'for' '(' (varDecl | exprStmt | ';') expression? ';' expression? ')' statement;
ifStmt: 'if' '(' expression ')' statement ('else' statement)?;
printStmt: 'print' expression ';';
returnStmt: 'return' expression? ';';
whileStmt: 'while' '(' expression ')' statement;
block: '{' declaration* '}';
funAnon: 'fun' '(' parameters? ')' block;
init: 'init' '(' parameters? ')' block;

expression: assignment | funAnon;

assignment: (call '.')? IDENTIFIER '=' assignment | logicOr;

logicOr: logicAnd ('or' logicAnd)*;
logicAnd: equality ('and' equality)*;
equality: comparison (( '!=' | '==') comparison)*;
comparison: term (( '>' | '>=' | '<' | '<=') term)*;
term: factor (( '-' | '+') factor)*;
factor: unary (( '/' | '*' | '%') unary)*;
array: '[' (expression (',' expression)*)? ']';
instantiation: 'new' IDENTIFIER '(' arguments? ')';

unary: ( '!' | '-') unary | call;

call:
	primary (
		'(' arguments? ')'
		| '.' IDENTIFIER
		| '[' expression ']'
	)*
	| funAnon;

primary:
	'true'
	| 'false'
	| 'nil'
	| 'this'
	| 'super' '.' IDENTIFIER
	| NUMBER
	| STRING
	| IDENTIFIER
	| '(' expression ')'
	| array
	| instantiation;

methods: (function | init)*;
function: IDENTIFIER '(' parameters? ')' block;
parameters: IDENTIFIER ( ',' IDENTIFIER)*;
arguments: expression ( ',' expression)*;

NUMBER: DIGIT+ ( '.' DIGIT+)?;
STRING: '"' (~["\\])* '"';
IDENTIFIER: ALPHA ( ALPHA | DIGIT)*;
fragment ALPHA: [a-zA-Z_];
fragment DIGIT: [0-9];
WS: [ \t\r\n]+ -> skip;
ONE_LINE_COMMENT: '//' (~ '\n')* '\n'? -> skip;
