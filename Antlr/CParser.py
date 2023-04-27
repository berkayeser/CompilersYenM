# Generated from Antlr/C.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,201,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,4,0,48,8,0,11,0,12,0,49,1,0,1,0,1,1,
        1,1,3,1,56,8,1,1,1,3,1,59,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,73,8,2,1,3,1,3,1,3,1,3,3,3,79,8,3,1,3,1,3,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,93,8,5,1,6,1,6,1,6,3,6,98,
        8,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,5,9,109,8,9,10,9,12,9,112,
        9,9,1,10,1,10,1,10,1,10,3,10,118,8,10,3,10,120,8,10,1,10,1,10,1,
        10,1,10,1,10,3,10,127,8,10,3,10,129,8,10,1,10,1,10,3,10,133,8,10,
        1,11,1,11,1,11,1,11,3,11,139,8,11,3,11,141,8,11,1,12,1,12,1,12,1,
        12,3,12,147,8,12,3,12,149,8,12,1,13,1,13,1,13,1,13,3,13,155,8,13,
        3,13,157,8,13,1,14,1,14,1,14,1,14,1,14,3,14,164,8,14,1,14,3,14,167,
        8,14,1,14,1,14,1,14,1,14,3,14,173,8,14,1,14,1,14,3,14,177,8,14,1,
        15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,
        20,1,21,1,21,1,21,1,21,3,21,197,8,21,1,22,1,22,1,22,0,0,23,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,6,1,
        0,26,27,1,0,15,18,1,0,7,8,2,0,9,10,13,13,2,0,7,8,11,12,2,0,21,21,
        23,25,206,0,47,1,0,0,0,2,58,1,0,0,0,4,72,1,0,0,0,6,74,1,0,0,0,8,
        82,1,0,0,0,10,92,1,0,0,0,12,97,1,0,0,0,14,99,1,0,0,0,16,102,1,0,
        0,0,18,106,1,0,0,0,20,132,1,0,0,0,22,134,1,0,0,0,24,142,1,0,0,0,
        26,150,1,0,0,0,28,176,1,0,0,0,30,178,1,0,0,0,32,180,1,0,0,0,34,182,
        1,0,0,0,36,184,1,0,0,0,38,186,1,0,0,0,40,188,1,0,0,0,42,196,1,0,
        0,0,44,198,1,0,0,0,46,48,3,2,1,0,47,46,1,0,0,0,48,49,1,0,0,0,49,
        47,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,52,5,0,0,1,52,1,1,0,0,
        0,53,55,3,4,2,0,54,56,3,8,4,0,55,54,1,0,0,0,55,56,1,0,0,0,56,59,
        1,0,0,0,57,59,3,8,4,0,58,53,1,0,0,0,58,57,1,0,0,0,59,3,1,0,0,0,60,
        61,3,10,5,0,61,62,5,1,0,0,62,73,1,0,0,0,63,64,3,12,6,0,64,65,5,1,
        0,0,65,73,1,0,0,0,66,67,3,20,10,0,67,68,5,1,0,0,68,73,1,0,0,0,69,
        70,3,6,3,0,70,71,5,1,0,0,71,73,1,0,0,0,72,60,1,0,0,0,72,63,1,0,0,
        0,72,66,1,0,0,0,72,69,1,0,0,0,73,5,1,0,0,0,74,75,5,2,0,0,75,78,5,
        3,0,0,76,79,5,22,0,0,77,79,3,44,22,0,78,76,1,0,0,0,78,77,1,0,0,0,
        79,80,1,0,0,0,80,81,5,4,0,0,81,7,1,0,0,0,82,83,7,0,0,0,83,9,1,0,
        0,0,84,85,3,12,6,0,85,86,5,20,0,0,86,87,3,20,10,0,87,93,1,0,0,0,
        88,89,3,16,8,0,89,90,5,20,0,0,90,91,3,20,10,0,91,93,1,0,0,0,92,84,
        1,0,0,0,92,88,1,0,0,0,93,11,1,0,0,0,94,98,3,14,7,0,95,98,3,42,21,
        0,96,98,5,22,0,0,97,94,1,0,0,0,97,95,1,0,0,0,97,96,1,0,0,0,98,13,
        1,0,0,0,99,100,3,18,9,0,100,101,5,22,0,0,101,15,1,0,0,0,102,103,
        5,19,0,0,103,104,3,18,9,0,104,105,5,22,0,0,105,17,1,0,0,0,106,110,
        7,1,0,0,107,109,5,9,0,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,
        1,0,0,0,110,111,1,0,0,0,111,19,1,0,0,0,112,110,1,0,0,0,113,119,3,
        22,11,0,114,117,3,30,15,0,115,118,3,22,11,0,116,118,3,20,10,0,117,
        115,1,0,0,0,117,116,1,0,0,0,118,120,1,0,0,0,119,114,1,0,0,0,119,
        120,1,0,0,0,120,133,1,0,0,0,121,122,5,3,0,0,122,128,3,22,11,0,123,
        126,3,30,15,0,124,127,3,22,11,0,125,127,3,20,10,0,126,124,1,0,0,
        0,126,125,1,0,0,0,127,129,1,0,0,0,128,123,1,0,0,0,128,129,1,0,0,
        0,129,130,1,0,0,0,130,131,5,4,0,0,131,133,1,0,0,0,132,113,1,0,0,
        0,132,121,1,0,0,0,133,21,1,0,0,0,134,140,3,24,12,0,135,138,3,32,
        16,0,136,139,3,24,12,0,137,139,3,22,11,0,138,136,1,0,0,0,138,137,
        1,0,0,0,139,141,1,0,0,0,140,135,1,0,0,0,140,141,1,0,0,0,141,23,1,
        0,0,0,142,148,3,26,13,0,143,146,3,34,17,0,144,147,3,26,13,0,145,
        147,3,24,12,0,146,144,1,0,0,0,146,145,1,0,0,0,147,149,1,0,0,0,148,
        143,1,0,0,0,148,149,1,0,0,0,149,25,1,0,0,0,150,156,3,28,14,0,151,
        154,3,36,18,0,152,155,3,28,14,0,153,155,3,26,13,0,154,152,1,0,0,
        0,154,153,1,0,0,0,155,157,1,0,0,0,156,151,1,0,0,0,156,157,1,0,0,
        0,157,27,1,0,0,0,158,164,5,22,0,0,159,160,5,3,0,0,160,161,3,22,11,
        0,161,162,5,4,0,0,162,164,1,0,0,0,163,158,1,0,0,0,163,159,1,0,0,
        0,164,166,1,0,0,0,165,167,5,14,0,0,166,165,1,0,0,0,166,167,1,0,0,
        0,167,177,1,0,0,0,168,177,3,42,21,0,169,177,3,44,22,0,170,173,3,
        40,20,0,171,173,3,38,19,0,172,170,1,0,0,0,172,171,1,0,0,0,173,174,
        1,0,0,0,174,175,3,28,14,0,175,177,1,0,0,0,176,163,1,0,0,0,176,168,
        1,0,0,0,176,169,1,0,0,0,176,172,1,0,0,0,177,29,1,0,0,0,178,179,5,
        6,0,0,179,31,1,0,0,0,180,181,5,5,0,0,181,33,1,0,0,0,182,183,7,2,
        0,0,183,35,1,0,0,0,184,185,7,3,0,0,185,37,1,0,0,0,186,187,7,4,0,
        0,187,39,1,0,0,0,188,189,5,3,0,0,189,190,7,1,0,0,190,191,5,4,0,0,
        191,41,1,0,0,0,192,193,5,9,0,0,193,197,5,22,0,0,194,195,5,9,0,0,
        195,197,3,42,21,0,196,192,1,0,0,0,196,194,1,0,0,0,197,43,1,0,0,0,
        198,199,7,5,0,0,199,45,1,0,0,0,24,49,55,58,72,78,92,97,110,117,119,
        126,128,132,138,140,146,148,154,156,163,166,172,176,196
    ]

class CParser ( Parser ):

    grammarFileName = "C.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'printf'", "'('", "')'", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'!'", "'&'", 
                     "'%'", "<INVALID>", "'int'", "'char'", "'bool'", "'float'", 
                     "'const'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMPOPS", "LOGICOPS", "PLUS", "MINUS", 
                      "STAR", "DIVIDE", "EXCLAMAION", "AMPERSAND", "PROCENT", 
                      "SPECIALUNARY", "INT", "CHAR", "BOOL", "FLOAT", "CONST", 
                      "EQUALS", "BOOLLITERAL", "IDENTIFIER", "INTLITERAL", 
                      "FLOATLITERAL", "CHARLITERAL", "SINGLECOMMENT", "MULTICOMMENT", 
                      "DIGIT", "WS", "ANY" ]

    RULE_run = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_print = 3
    RULE_comment = 4
    RULE_assignment = 5
    RULE_declaration = 6
    RULE_instantiation = 7
    RULE_const_instantiation = 8
    RULE_type = 9
    RULE_logicexpression = 10
    RULE_boolexpression = 11
    RULE_term = 12
    RULE_factor = 13
    RULE_element = 14
    RULE_logicops = 15
    RULE_compops = 16
    RULE_termops = 17
    RULE_factorops = 18
    RULE_unaryops = 19
    RULE_typecast = 20
    RULE_pointer = 21
    RULE_literal = 22

    ruleNames =  [ "run", "line", "statement", "print", "comment", "assignment", 
                   "declaration", "instantiation", "const_instantiation", 
                   "type", "logicexpression", "boolexpression", "term", 
                   "factor", "element", "logicops", "compops", "termops", 
                   "factorops", "unaryops", "typecast", "pointer", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    COMPOPS=5
    LOGICOPS=6
    PLUS=7
    MINUS=8
    STAR=9
    DIVIDE=10
    EXCLAMAION=11
    AMPERSAND=12
    PROCENT=13
    SPECIALUNARY=14
    INT=15
    CHAR=16
    BOOL=17
    FLOAT=18
    CONST=19
    EQUALS=20
    BOOLLITERAL=21
    IDENTIFIER=22
    INTLITERAL=23
    FLOATLITERAL=24
    CHARLITERAL=25
    SINGLECOMMENT=26
    MULTICOMMENT=27
    DIGIT=28
    WS=29
    ANY=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.LineContext)
            else:
                return self.getTypedRuleContext(CParser.LineContext,i)


        def getRuleIndex(self):
            return CParser.RULE_run

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRun" ):
                listener.enterRun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRun" ):
                listener.exitRun(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRun" ):
                return visitor.visitRun(self)
            else:
                return visitor.visitChildren(self)




    def run(self):

        localctx = CParser.RunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_run)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.line()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 267361164) != 0)):
                    break

            self.state = 51
            self.match(CParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)


        def comment(self):
            return self.getTypedRuleContext(CParser.CommentContext,0)


        def getRuleIndex(self):
            return CParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = CParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 7, 8, 9, 11, 12, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.statement()
                self.state = 55
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 54
                    self.comment()


                pass
            elif token in [26, 27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.comment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(CParser.AssignmentContext,0)


        def declaration(self):
            return self.getTypedRuleContext(CParser.DeclarationContext,0)


        def logicexpression(self):
            return self.getTypedRuleContext(CParser.LogicexpressionContext,0)


        def print_(self):
            return self.getTypedRuleContext(CParser.PrintContext,0)


        def getRuleIndex(self):
            return CParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.assignment()
                self.state = 61
                self.match(CParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.declaration()
                self.state = 64
                self.match(CParser.T__0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.logicexpression()
                self.state = 67
                self.match(CParser.T__0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.print_()
                self.state = 70
                self.match(CParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(CParser.LiteralContext,0)


        def getRuleIndex(self):
            return CParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = CParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(CParser.T__1)
            self.state = 75
            self.match(CParser.T__2)
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 76
                self.match(CParser.IDENTIFIER)
                pass
            elif token in [21, 23, 24, 25]:
                self.state = 77
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 80
            self.match(CParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLECOMMENT(self):
            return self.getToken(CParser.SINGLECOMMENT, 0)

        def MULTICOMMENT(self):
            return self.getToken(CParser.MULTICOMMENT, 0)

        def getRuleIndex(self):
            return CParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = CParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(CParser.DeclarationContext,0)


        def EQUALS(self):
            return self.getToken(CParser.EQUALS, 0)

        def logicexpression(self):
            return self.getTypedRuleContext(CParser.LogicexpressionContext,0)


        def const_instantiation(self):
            return self.getTypedRuleContext(CParser.Const_instantiationContext,0)


        def getRuleIndex(self):
            return CParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = CParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 15, 16, 17, 18, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.declaration()
                self.state = 85
                self.match(CParser.EQUALS)
                self.state = 86
                self.logicexpression()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.const_instantiation()
                self.state = 89
                self.match(CParser.EQUALS)
                self.state = 90
                self.logicexpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instantiation(self):
            return self.getTypedRuleContext(CParser.InstantiationContext,0)


        def pointer(self):
            return self.getTypedRuleContext(CParser.PointerContext,0)


        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = CParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declaration)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.instantiation()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.pointer()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.match(CParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstantiationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CParser.RULE_instantiation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstantiation" ):
                listener.enterInstantiation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstantiation" ):
                listener.exitInstantiation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstantiation" ):
                return visitor.visitInstantiation(self)
            else:
                return visitor.visitChildren(self)




    def instantiation(self):

        localctx = CParser.InstantiationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_instantiation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.type_()
            self.state = 100
            self.match(CParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_instantiationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CParser.CONST, 0)

        def type_(self):
            return self.getTypedRuleContext(CParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CParser.RULE_const_instantiation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst_instantiation" ):
                listener.enterConst_instantiation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst_instantiation" ):
                listener.exitConst_instantiation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_instantiation" ):
                return visitor.visitConst_instantiation(self)
            else:
                return visitor.visitChildren(self)




    def const_instantiation(self):

        localctx = CParser.Const_instantiationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_const_instantiation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(CParser.CONST)
            self.state = 103
            self.type_()
            self.state = 104
            self.match(CParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CParser.INT, 0)

        def CHAR(self):
            return self.getToken(CParser.CHAR, 0)

        def FLOAT(self):
            return self.getToken(CParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CParser.BOOL, 0)

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(CParser.STAR)
            else:
                return self.getToken(CParser.STAR, i)

        def getRuleIndex(self):
            return CParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = CParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 107
                self.match(CParser.STAR)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolexpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.BoolexpressionContext)
            else:
                return self.getTypedRuleContext(CParser.BoolexpressionContext,i)


        def logicops(self):
            return self.getTypedRuleContext(CParser.LogicopsContext,0)


        def logicexpression(self):
            return self.getTypedRuleContext(CParser.LogicexpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_logicexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicexpression" ):
                listener.enterLogicexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicexpression" ):
                listener.exitLogicexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicexpression" ):
                return visitor.visitLogicexpression(self)
            else:
                return visitor.visitChildren(self)




    def logicexpression(self):

        localctx = CParser.LogicexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_logicexpression)
        self._la = 0 # Token type
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.boolexpression()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 114
                    self.logicops()
                    self.state = 117
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        self.state = 115
                        self.boolexpression()
                        pass

                    elif la_ == 2:
                        self.state = 116
                        self.logicexpression()
                        pass




                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(CParser.T__2)
                self.state = 122
                self.boolexpression()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 123
                    self.logicops()
                    self.state = 126
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        self.state = 124
                        self.boolexpression()
                        pass

                    elif la_ == 2:
                        self.state = 125
                        self.logicexpression()
                        pass




                self.state = 130
                self.match(CParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.TermContext)
            else:
                return self.getTypedRuleContext(CParser.TermContext,i)


        def compops(self):
            return self.getTypedRuleContext(CParser.CompopsContext,0)


        def boolexpression(self):
            return self.getTypedRuleContext(CParser.BoolexpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_boolexpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolexpression" ):
                listener.enterBoolexpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolexpression" ):
                listener.exitBoolexpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolexpression" ):
                return visitor.visitBoolexpression(self)
            else:
                return visitor.visitChildren(self)




    def boolexpression(self):

        localctx = CParser.BoolexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_boolexpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.term()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 135
                self.compops()
                self.state = 138
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 136
                    self.term()
                    pass

                elif la_ == 2:
                    self.state = 137
                    self.boolexpression()
                    pass




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.FactorContext)
            else:
                return self.getTypedRuleContext(CParser.FactorContext,i)


        def termops(self):
            return self.getTypedRuleContext(CParser.TermopsContext,0)


        def term(self):
            return self.getTypedRuleContext(CParser.TermContext,0)


        def getRuleIndex(self):
            return CParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = CParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.factor()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==8:
                self.state = 143
                self.termops()
                self.state = 146
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 144
                    self.factor()
                    pass

                elif la_ == 2:
                    self.state = 145
                    self.term()
                    pass




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ElementContext)
            else:
                return self.getTypedRuleContext(CParser.ElementContext,i)


        def factorops(self):
            return self.getTypedRuleContext(CParser.FactoropsContext,0)


        def factor(self):
            return self.getTypedRuleContext(CParser.FactorContext,0)


        def getRuleIndex(self):
            return CParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = CParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.element()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9728) != 0):
                self.state = 151
                self.factorops()
                self.state = 154
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 152
                    self.element()
                    pass

                elif la_ == 2:
                    self.state = 153
                    self.factor()
                    pass




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def boolexpression(self):
            return self.getTypedRuleContext(CParser.BoolexpressionContext,0)


        def SPECIALUNARY(self):
            return self.getToken(CParser.SPECIALUNARY, 0)

        def pointer(self):
            return self.getTypedRuleContext(CParser.PointerContext,0)


        def literal(self):
            return self.getTypedRuleContext(CParser.LiteralContext,0)


        def element(self):
            return self.getTypedRuleContext(CParser.ElementContext,0)


        def typecast(self):
            return self.getTypedRuleContext(CParser.TypecastContext,0)


        def unaryops(self):
            return self.getTypedRuleContext(CParser.UnaryopsContext,0)


        def getRuleIndex(self):
            return CParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = CParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [22]:
                    self.state = 158
                    self.match(CParser.IDENTIFIER)
                    pass
                elif token in [3]:
                    self.state = 159
                    self.match(CParser.T__2)
                    self.state = 160
                    self.boolexpression()
                    self.state = 161
                    self.match(CParser.T__3)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 165
                    self.match(CParser.SPECIALUNARY)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.pointer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 172
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 170
                    self.typecast()
                    pass
                elif token in [7, 8, 11, 12]:
                    self.state = 171
                    self.unaryops()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 174
                self.element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicopsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGICOPS(self):
            return self.getToken(CParser.LOGICOPS, 0)

        def getRuleIndex(self):
            return CParser.RULE_logicops

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicops" ):
                listener.enterLogicops(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicops" ):
                listener.exitLogicops(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicops" ):
                return visitor.visitLogicops(self)
            else:
                return visitor.visitChildren(self)




    def logicops(self):

        localctx = CParser.LogicopsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_logicops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(CParser.LOGICOPS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompopsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPOPS(self):
            return self.getToken(CParser.COMPOPS, 0)

        def getRuleIndex(self):
            return CParser.RULE_compops

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompops" ):
                listener.enterCompops(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompops" ):
                listener.exitCompops(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompops" ):
                return visitor.visitCompops(self)
            else:
                return visitor.visitChildren(self)




    def compops(self):

        localctx = CParser.CompopsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_compops)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(CParser.COMPOPS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermopsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(CParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(CParser.PLUS, 0)

        def getRuleIndex(self):
            return CParser.RULE_termops

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermops" ):
                listener.enterTermops(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermops" ):
                listener.exitTermops(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermops" ):
                return visitor.visitTermops(self)
            else:
                return visitor.visitChildren(self)




    def termops(self):

        localctx = CParser.TermopsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_termops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactoropsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(CParser.STAR, 0)

        def DIVIDE(self):
            return self.getToken(CParser.DIVIDE, 0)

        def PROCENT(self):
            return self.getToken(CParser.PROCENT, 0)

        def getRuleIndex(self):
            return CParser.RULE_factorops

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorops" ):
                listener.enterFactorops(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorops" ):
                listener.exitFactorops(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorops" ):
                return visitor.visitFactorops(self)
            else:
                return visitor.visitChildren(self)




    def factorops(self):

        localctx = CParser.FactoropsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_factorops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9728) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryopsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(CParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(CParser.PLUS, 0)

        def EXCLAMAION(self):
            return self.getToken(CParser.EXCLAMAION, 0)

        def AMPERSAND(self):
            return self.getToken(CParser.AMPERSAND, 0)

        def getRuleIndex(self):
            return CParser.RULE_unaryops

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryops" ):
                listener.enterUnaryops(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryops" ):
                listener.exitUnaryops(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryops" ):
                return visitor.visitUnaryops(self)
            else:
                return visitor.visitChildren(self)




    def unaryops(self):

        localctx = CParser.UnaryopsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unaryops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6528) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypecastContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CParser.INT, 0)

        def CHAR(self):
            return self.getToken(CParser.CHAR, 0)

        def FLOAT(self):
            return self.getToken(CParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CParser.BOOL, 0)

        def getRuleIndex(self):
            return CParser.RULE_typecast

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypecast" ):
                listener.enterTypecast(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypecast" ):
                listener.exitTypecast(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypecast" ):
                return visitor.visitTypecast(self)
            else:
                return visitor.visitChildren(self)




    def typecast(self):

        localctx = CParser.TypecastContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_typecast)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(CParser.T__2)
            self.state = 189
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 190
            self.match(CParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(CParser.STAR, 0)

        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def pointer(self):
            return self.getTypedRuleContext(CParser.PointerContext,0)


        def getRuleIndex(self):
            return CParser.RULE_pointer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointer" ):
                listener.enterPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointer" ):
                listener.exitPointer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointer" ):
                return visitor.visitPointer(self)
            else:
                return visitor.visitChildren(self)




    def pointer(self):

        localctx = CParser.PointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_pointer)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(CParser.STAR)
                self.state = 193
                self.match(CParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(CParser.STAR)
                self.state = 195
                self.pointer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLLITERAL(self):
            return self.getToken(CParser.BOOLLITERAL, 0)

        def INTLITERAL(self):
            return self.getToken(CParser.INTLITERAL, 0)

        def FLOATLITERAL(self):
            return self.getToken(CParser.FLOATLITERAL, 0)

        def CHARLITERAL(self):
            return self.getToken(CParser.CHARLITERAL, 0)

        def getRuleIndex(self):
            return CParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60817408) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





