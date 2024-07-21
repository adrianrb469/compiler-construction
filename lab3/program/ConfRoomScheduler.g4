grammar ConfRoomScheduler;

prog: stat+ EOF;

stat:
	reserve NEWLINE?	    # reserveStat
	| cancel NEWLINE?	    # cancelStat
    | list NEWLINE?		    # listStat
    | reschedule NEWLINE?	# rescheduleStat
	| NEWLINE			    # blank;

reserve:
	'RESERVE' NAME 'ROOM' ID 'AT' DATE 'FROM' TIME 'TO' TIME 'EVENT' STRING 'TYPE' STRING (
		'DESCRIPTION' STRING
	)?;

cancel: 'CANCEL' INT;
list: 'LIST';
reschedule: 'RESCHEDULE' INT 'TO' DATE 'FROM' TIME 'TO' TIME;

NAME: [a-zA-Z]+;
INT: [0-9]+;
ID: [a-zA-Z0-9]+;
DATE: DIGIT DIGIT '/' DIGIT DIGIT '/' DIGIT DIGIT DIGIT DIGIT;
TIME: DIGIT DIGIT ':' DIGIT DIGIT;
STRING: '"' (~["\r\n])* '"';
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;

fragment DIGIT: [0-9];
