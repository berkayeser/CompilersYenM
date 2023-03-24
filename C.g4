grammar C;


run
    : line+;

line
    : statement comment?
    | comment;

statement
    : assignment ';'
    | declaration ';'
    | expression ';'
    | 'printf' '(' (IDENTIFIER | LITERAL) ')' ';'';

comment
    : SINGLECOMMENT
    | MULTICOMMENT;

assignment
    : declaration EQUALS expression;

declaration
    : instantiation
    | IDENTIFIER
    | POINTER;

instantiation
    : CONST? TYPE IDENTIFIER;

expression
    : '('? (compexpression | term ) ')'?;

compexpression
    : term ((LOGICOPS | COMPOPS) term)+;

term
    : factor (TERMOPS factor)*;

factor
    : element (FACTOROPS element)*;

element
    : UNARYOPS? (LITERAL | IDENTIFIER | '(' expression ')') SPECIALUNARY?;

COMPOPS
    : '<' | '>' | '<=' | '>=' | '==' | '!=';

LOGICOPS
    : '&&' | '||';

TYPE
    : (INT | CHAR | FLOAT) '*'*;

TERMOPS
    : '+' | '-';

FACTOROPS
    : '*' | '/' | '%';

UNARYOPS
    : '+' | '-' | '!' | '*' | '&';

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

LITERAL
    : 'true'
    | 'false'
    | DIGIT+ ((',' | '.') DIGIT+)?
    | SINGLESTRING
    | DOUBLESTRING;

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
