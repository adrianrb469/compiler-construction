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
	| INT					# int
	| ID					# id
	| '(' expr ')'			# parens
	| expr compareOp expr	# compare;

compareOp: '==' | '!=' | '<' | '<=' | '>' | '>=';

constant: INT | STRING;

MUL: '*'; // define token for multiplication
DIV: '/'; // define token for division
ADD: '+'; // define token for addition
SUB: '-'; // define token for subtraction
ID: [a-zA-Z]+; // match identifiers
INT: [0-9]+; // match integers

STRING: ('"' ~'"'* '"'); // basically, anything between double quotes that isn't a double quote

NEWLINE:
	'\r'? '\n'; // return newlines to parser (is end-statement signal)
COMMENT: '//' ~[\r\n]* -> skip; // match inline comments

WS: [ \t]+ -> skip; // toss out whitespace

INVALID_CHAR:
	.; // match any single character that is not in the grammar
