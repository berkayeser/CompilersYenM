grammar C;


run
    : line+;

line
    : statement comment?
    | comment;

statement
    : assignment ';'
    | declaration ';'
    | boolexpression ';'
    | 'printf' '(' (IDENTIFIER | LITERAL) ')' ';';

comment
    : SINGLECOMMENT
    | MULTICOMMENT;

assignment
    : declaration EQUALS boolexpression;

declaration
    : instantiation
    | IDENTIFIER
    | POINTER;

instantiation
    : CONST? TYPE IDENTIFIER;

boolexpression
    : '('? term (BOOLOPS (term | boolexpression))? ')'?;

term
    : factor (TERMOPS (factor | term))?;

factor
    : element (FACTOROPS (element | factor))?;

element
    : (UNARYOPS)? (literal | IDENTIFIER | POINTER | '(' boolexpression ')') SPECIALUNARY?;

BOOLOPS
    : LOGICOPS
    | COMPOPS;

COMPOPS
    : '<' | '>' | '<=' | '>=' | '==' | '!=';

LOGICOPS
    : '&&' | '||';

TYPE
    : (INT | CHAR | FLOAT) '*'*;

UNARYOPS
    : '-' | '!' | '&';

TERMOPS
    : '+' | '-';

FACTOROPS
    : '*' | '/' | '%';

SPECIALUNARY
    : '++' | '--';

INT : 'int';
CHAR : 'char';
FLOAT : 'float';
CONST : 'const';
EQUALS : '=';

POINTER
    : '*'+ IDENTIFIER;

IDENTIFIER
    : ('_' | [a-zA-Z]) ('_' | [0-9] | [a-zA-Z])*;

literal
    : TRUE
    | FALSE
    | FLOAT
    | INT
    | DIGIT+ ((',' | '.') DIGIT+)?
    | CHAR
    | SINGLESTRING
    | DOUBLESTRING;

TRUE: 'true';

FALSE: 'false';

SINGLESTRING
    : '\'' .*? '\'';

DOUBLESTRING
    : '"' .*? '"';

SINGLECOMMENT
    : '//' ~[\r\n]* ('\r' | '\n');

MULTICOMMENT
    : '/*' .*? '*/';

DIGIT: [0-9];

WS: [ \t\r\n]+ -> skip;
