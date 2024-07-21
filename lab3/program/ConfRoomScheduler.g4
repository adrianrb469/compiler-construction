grammar ConfRoomScheduler;

prog: stat+;

stat:
	reserve NEWLINE		# reserveStat
	| cancel NEWLINE	# cancelStat
	| NEWLINE			# blank;

reserve:
	'RESERVE' NAME 'ROOM' ID 'AT' DATE 'FROM' TIME 'TO' TIME 'EVENT' STRING (
		'DESCRIPTION' STRING
	)?;

cancel: 'CANCEL' INT;

NAME: [a-zA-Z]+;
INT: [0-9]+;
ID: [a-zA-Z0-9]+;
DATE: DIGIT DIGIT '/' DIGIT DIGIT '/' DIGIT DIGIT DIGIT DIGIT;
TIME: DIGIT DIGIT ':' DIGIT DIGIT;
STRING: '"' (~["\r\n])* '"';
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;

fragment DIGIT: [0-9];

// antlr -Dlanguage=Python3 MiniLang.g4 python3 DriverConfroom.py program_test_confroom.txt
