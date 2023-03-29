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
    | 'printf' '(' (IDENTIFIER | literal) ')' ';';

comment
    : SINGLECOMMENT
    | MULTICOMMENT;

assignment
    : declaration EQUALS logicexpression;

declaration
    : instantiation
    | IDENTIFIER
    | POINTER;

instantiation
    : CONST? TYPE IDENTIFIER;

logicexpression
    : '('? boolexpression (LOGICOPS (boolexpression | logicexpression))? ')'?;

boolexpression
    : term (COMPOPS (term | boolexpression))?;

term
    : factor (TERMOPS (factor | term))?;

factor
    : element (FACTOROPS (element | factor))?;

element
    : (UNARYOPS)? (literal | IDENTIFIER | POINTER | '(' boolexpression ')') SPECIALUNARY?;

COMPOPS
    : '<' | '>' | '<=' | '>=' | '==' | '!=';

LOGICOPS
    : '&&' | '||';

TYPE
    : (INT | CHAR | FLOAT | BOOL) '*'*;

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
BOOL : 'bool';
FLOAT : 'float';
CONST : 'const';
EQUALS : '=';

POINTER
    : '*'+ IDENTIFIER;

IDENTIFIER
    : ('_' | [a-zA-Z]) ('_' | [0-9] | [a-zA-Z])*;

literal
    : BOOLLITERAL
    | INTLITERAL
    | FLOATLITERAL
    | CHARLITERAL
    | STRINGLITERAL;

INTLITERAL
    : DIGIT+;

FLOATLITERAL
    : DIGIT+ ((',' | '.') DIGIT+)?;

BOOLLITERAL
    : 'true' | 'false';

CHARLITERAL
    : '\'' . '\'';

STRINGLITERAL
    : SINGLESTRING
    | DOUBLESTRING;

SINGLESTRING
    : '\'' . . .*? '\'';

DOUBLESTRING
    : '"' .*? '"';

SINGLECOMMENT
    : '//' ~[\r\n]* ('\r' | '\n');

MULTICOMMENT
    : '/*' .*? '*/';

DIGIT: [0-9];

WS: [ \t\r\n]+ -> skip;
