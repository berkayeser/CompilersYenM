# CompilersYenM

Simple C Compiler project by
  Youssef El Aseri \
  and \
  Berkay Eser
<br><br>

We ondersteunen Constant Folding, Constant Propagation, ...
<br><br>

#### Project 1

Alles geïmplementeerd
<br><br>

#### Project 2
Alles behalve Error Checking op
operaties van incompatibele types. Dit begrepen we niet goed.
Bij constant propagation, passen we dit nergens meer toe 
als de variabele ergens geassigned wordt.<br>
BV: het volgende stukje code blijft onveranderd<br>
`int x = 1;   
int y = x  + 1;
x = 4`
<br><br>

#### Project 3
De grammar en llvm code zonder variables