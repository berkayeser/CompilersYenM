grammar C;


run
    : statement* EOF;

statement
    : comment? expression_statement SEMICOLON
    | comment? jump_statement SEMICOLON
    | comment? compound_statement
    | comment? block_scope
    | comment;

block_scope
    : LCURLY statement* RCURLY;

compound_statement
    : if
    | while
    | for;

expression_statement
    : assignment
    | declaration
    | logicexpression
    | print;

jump_statement
    : break
    | continue;

if
    : IF condition block_scope else?;

else
    : ELSE block_scope;

while
    : WHILE condition block_scope;

for
    : FOR for_condition block_scope;

break
    : BREAK;

continue
    : CONTINUE;

condition
    : LBRACKET logicexpression RBRACKET;

for_condition
    : LBRACKET assignment SEMICOLON logicexpression SEMICOLON update_expression RBRACKET;

update_expression
    : ((IDENTIFIER | pointer) EQUALS)? logicexpression;
//    | ((IDENTIFIER | pointer) EQUALS)? logicexpression COMMA update_expression;

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
    : IDENTIFIER | '(' boolexpression ')'
    | IDENTIFIER SPECIALUNARY
    | SPECIALUNARY IDENTIFIER
    | '(' boolexpression ')'
    | pointer
    | literal
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

literal
    : BOOLLITERAL
    | INTLITERAL
    | FLOATLITERAL
    | CHARLITERAL;

IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
BREAK: 'break';
CONTINUE: 'continue';

COMPOPS
    : '<' | '>' | '<=' | '>=' | '==' | '!=';

LOGICOPS
    : '&&' | '||';

EQUALS : '=';
SEMICOLON: ';';
LBRACKET: '(';
RBRACKET: ')';
LCURLY: '{';
RCURLY: '}';
COMMA: ',';

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



IDENTIFIER
    : ('_' | [a-zA-Z]) ('_' | [0-9] | [a-zA-Z])*;

FLOATLITERAL
    : DIGIT+ ((',' | '.') DIGIT+)?;

INTLITERAL
    : DIGIT+;

CHARLITERAL
    : '\'' '\\'? . '\'';

BOOLLITERAL
    : 'true' | 'false';

SINGLECOMMENT
    : '//' ~[\r\n]* ('\r' | '\n')?;

MULTICOMMENT
    : '/*' .*? '*/';

fragment DIGIT: [0-9];

WS: [ \t\r\n]+ -> skip;

ANY : .;