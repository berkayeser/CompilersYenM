grammar C;


run
    : line+ EOF;

line
    : statement comment?
    | comment;

statement
    : assignment ';'
    | declaration ';'
    | logicexpression ';'
    | print ';' ;

print
    : 'printf' '(' (IDENTIFIER | literal) ')';

comment
    : SINGLECOMMENT
    | MULTICOMMENT;

assignment
    : declaration EQUALS logicexpression
    | const_instantiation EQUALS logicexpression
    | rvalue_assignment;

rvalue_assignment
    : logicexpression EQUALS logicexpression;

declaration
    : instantiation
    | pointer
    | IDENTIFIER;

instantiation
    : type IDENTIFIER;

const_instantiation
    : CONST type IDENTIFIER;

type
    : (INT | CHAR | FLOAT | BOOL) STAR*;

logicexpression
    :  boolexpression (logicops (boolexpression | logicexpression))?
    | '(' boolexpression (logicops (boolexpression | logicexpression))? ')';

boolexpression
    : term (compops (term | boolexpression))?;

term
    : factor (termops (factor | term))?;

factor
    : element (factorops (element | factor))?;

element
    : ( IDENTIFIER | '(' boolexpression ')') SPECIALUNARY? | pointer | literal
    | (typecast | unaryops) element;


logicops
    : LOGICOPS;

compops
    : COMPOPS;

termops
    : MINUS
    | PLUS;

factorops
    : STAR
    | DIVIDE
    | PROCENT;

unaryops
    : MINUS | PLUS | EXCLAMAION | AMPERSAND;

typecast
    : '(' (INT | CHAR | FLOAT | BOOL) ')';

pointer
    : STAR IDENTIFIER
    | STAR pointer;

COMPOPS
    : '<' | '>' | '<=' | '>=' | '==' | '!=';

LOGICOPS
    : '&&' | '||';



PLUS : '+';
MINUS : '-';
STAR : '*';
DIVIDE : '/';
EXCLAMAION : '!';
AMPERSAND : '&';
PROCENT : '%';

SPECIALUNARY
    : '++' | '--';

INT : 'int';
CHAR : 'char';
BOOL : 'bool';
FLOAT : 'float';
CONST : 'const';
EQUALS : '=';

literal
    : BOOLLITERAL
    | INTLITERAL
    | FLOATLITERAL
    | CHARLITERAL;

BOOLLITERAL
    : 'true' | 'false';

IDENTIFIER
    : ('_' | [a-zA-Z]) ('_' | [0-9] | [a-zA-Z])*;


INTLITERAL
    : DIGIT+;

FLOATLITERAL
    : DIGIT+ ((',' | '.') DIGIT+)?;



CHARLITERAL
    : '\'' '\\'? . '\'';

SINGLECOMMENT
    : '//' ~[\r\n]* ('\r' | '\n')?;

MULTICOMMENT
    : '/*' .*? '*/';

DIGIT: [0-9];

WS: [ \t\r\n]+ -> skip;

ANY : .;