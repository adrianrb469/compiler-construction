grammar ConfRoomScheduler;

prog: stat+ ;

stat: reserve NEWLINE                # reserveStat
    | cancel NEWLINE                 # cancelStat
    | NEWLINE                        # blank
    ;

reserve:
    'RESERVAR' ID 'PARA' DATE 'DE' TIME 'A' TIME 'EVENTO' STRING
    | 'RESERVAR' ID 'PARA' DATE 'DE' TIME 'A' TIME 'EVENTO' STRING 'DESCRIPCION' STRING
; 

cancel: 'CANCELAR' INT ;

INT: [0-9]+ ;
ID  : [a-zA-Z0-9]+ ; 
DATE: DIGIT DIGIT '/' DIGIT DIGIT '/' DIGIT DIGIT DIGIT DIGIT ; 
TIME: DIGIT DIGIT ':' DIGIT DIGIT ; 
STRING: ('"' ~'"'* '"'); // basically, anything between double quotes that isn't a double quote
NEWLINE: '\r'? '\n' ; 
WS  : [ \t]+ -> skip ;

fragment DIGIT : [0-9] ;
