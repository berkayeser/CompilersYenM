# Generated from C.g4 by ANTLR 4.12.0
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
        4,1,30,145,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,4,0,32,8,0,11,0,12,0,33,1,1,1,1,3,1,38,8,1,1,1,3,1,
        41,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,55,8,
        2,1,3,1,3,1,3,1,3,3,3,61,8,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,3,5,76,8,5,1,6,1,6,1,6,3,6,81,8,6,1,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,9,3,9,91,8,9,1,9,1,9,1,9,1,9,3,9,97,8,9,3,9,99,8,
        9,1,9,3,9,102,8,9,1,10,1,10,1,10,1,10,3,10,108,8,10,3,10,110,8,10,
        1,11,1,11,1,11,1,11,3,11,116,8,11,3,11,118,8,11,1,12,1,12,1,12,1,
        12,3,12,124,8,12,3,12,126,8,12,1,13,3,13,129,8,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,3,13,138,8,13,1,13,3,13,141,8,13,1,14,1,14,1,
        14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,2,1,0,27,28,
        1,0,20,24,154,0,31,1,0,0,0,2,40,1,0,0,0,4,54,1,0,0,0,6,56,1,0,0,
        0,8,65,1,0,0,0,10,75,1,0,0,0,12,80,1,0,0,0,14,82,1,0,0,0,16,85,1,
        0,0,0,18,90,1,0,0,0,20,103,1,0,0,0,22,111,1,0,0,0,24,119,1,0,0,0,
        26,128,1,0,0,0,28,142,1,0,0,0,30,32,3,2,1,0,31,30,1,0,0,0,32,33,
        1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,1,1,0,0,0,35,37,3,4,2,0,36,
        38,3,8,4,0,37,36,1,0,0,0,37,38,1,0,0,0,38,41,1,0,0,0,39,41,3,8,4,
        0,40,35,1,0,0,0,40,39,1,0,0,0,41,3,1,0,0,0,42,43,3,10,5,0,43,44,
        5,1,0,0,44,55,1,0,0,0,45,46,3,12,6,0,46,47,5,1,0,0,47,55,1,0,0,0,
        48,49,3,18,9,0,49,50,5,1,0,0,50,55,1,0,0,0,51,52,3,6,3,0,52,53,5,
        1,0,0,53,55,1,0,0,0,54,42,1,0,0,0,54,45,1,0,0,0,54,48,1,0,0,0,54,
        51,1,0,0,0,55,5,1,0,0,0,56,57,5,2,0,0,57,60,5,3,0,0,58,61,5,19,0,
        0,59,61,3,28,14,0,60,58,1,0,0,0,60,59,1,0,0,0,61,62,1,0,0,0,62,63,
        5,4,0,0,63,64,5,1,0,0,64,7,1,0,0,0,65,66,7,0,0,0,66,9,1,0,0,0,67,
        68,3,12,6,0,68,69,5,17,0,0,69,70,3,18,9,0,70,76,1,0,0,0,71,72,3,
        16,8,0,72,73,5,17,0,0,73,74,3,18,9,0,74,76,1,0,0,0,75,67,1,0,0,0,
        75,71,1,0,0,0,76,11,1,0,0,0,77,81,3,14,7,0,78,81,5,19,0,0,79,81,
        5,18,0,0,80,77,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,13,1,0,0,0,
        82,83,5,7,0,0,83,84,5,19,0,0,84,15,1,0,0,0,85,86,5,16,0,0,86,87,
        5,7,0,0,87,88,5,19,0,0,88,17,1,0,0,0,89,91,5,3,0,0,90,89,1,0,0,0,
        90,91,1,0,0,0,91,92,1,0,0,0,92,98,3,20,10,0,93,96,5,6,0,0,94,97,
        3,20,10,0,95,97,3,18,9,0,96,94,1,0,0,0,96,95,1,0,0,0,97,99,1,0,0,
        0,98,93,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,102,5,4,0,0,101,
        100,1,0,0,0,101,102,1,0,0,0,102,19,1,0,0,0,103,109,3,22,11,0,104,
        107,5,5,0,0,105,108,3,22,11,0,106,108,3,20,10,0,107,105,1,0,0,0,
        107,106,1,0,0,0,108,110,1,0,0,0,109,104,1,0,0,0,109,110,1,0,0,0,
        110,21,1,0,0,0,111,117,3,24,12,0,112,115,5,9,0,0,113,116,3,24,12,
        0,114,116,3,22,11,0,115,113,1,0,0,0,115,114,1,0,0,0,116,118,1,0,
        0,0,117,112,1,0,0,0,117,118,1,0,0,0,118,23,1,0,0,0,119,125,3,26,
        13,0,120,123,5,10,0,0,121,124,3,26,13,0,122,124,3,24,12,0,123,121,
        1,0,0,0,123,122,1,0,0,0,124,126,1,0,0,0,125,120,1,0,0,0,125,126,
        1,0,0,0,126,25,1,0,0,0,127,129,5,8,0,0,128,127,1,0,0,0,128,129,1,
        0,0,0,129,137,1,0,0,0,130,138,3,28,14,0,131,138,5,19,0,0,132,138,
        5,18,0,0,133,134,5,3,0,0,134,135,3,20,10,0,135,136,5,4,0,0,136,138,
        1,0,0,0,137,130,1,0,0,0,137,131,1,0,0,0,137,132,1,0,0,0,137,133,
        1,0,0,0,138,140,1,0,0,0,139,141,5,11,0,0,140,139,1,0,0,0,140,141,
        1,0,0,0,141,27,1,0,0,0,142,143,7,1,0,0,143,29,1,0,0,0,20,33,37,40,
        54,60,75,80,90,96,98,101,107,109,115,117,123,125,128,137,140
    ]

class CParser ( Parser ):

    grammarFileName = "C.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'printf'", "'('", "')'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'int'", "'char'", "'bool'", 
                     "'float'", "'const'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMPOPS", "LOGICOPS", "TYPE", "UNARYOPS", 
                      "TERMOPS", "FACTOROPS", "SPECIALUNARY", "INT", "CHAR", 
                      "BOOL", "FLOAT", "CONST", "EQUALS", "POINTER", "IDENTIFIER", 
                      "INTLITERAL", "FLOATLITERAL", "BOOLLITERAL", "CHARLITERAL", 
                      "STRINGLITERAL", "SINGLESTRING", "DOUBLESTRING", "SINGLECOMMENT", 
                      "MULTICOMMENT", "DIGIT", "WS" ]

    RULE_run = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_print = 3
    RULE_comment = 4
    RULE_assignment = 5
    RULE_declaration = 6
    RULE_instantiation = 7
    RULE_const_instantiation = 8
    RULE_logicexpression = 9
    RULE_boolexpression = 10
    RULE_term = 11
    RULE_factor = 12
    RULE_element = 13
    RULE_literal = 14

    ruleNames =  [ "run", "line", "statement", "print", "comment", "assignment", 
                   "declaration", "instantiation", "const_instantiation", 
                   "logicexpression", "boolexpression", "term", "factor", 
                   "element", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    COMPOPS=5
    LOGICOPS=6
    TYPE=7
    UNARYOPS=8
    TERMOPS=9
    FACTOROPS=10
    SPECIALUNARY=11
    INT=12
    CHAR=13
    BOOL=14
    FLOAT=15
    CONST=16
    EQUALS=17
    POINTER=18
    IDENTIFIER=19
    INTLITERAL=20
    FLOATLITERAL=21
    BOOLLITERAL=22
    CHARLITERAL=23
    STRINGLITERAL=24
    SINGLESTRING=25
    DOUBLESTRING=26
    SINGLECOMMENT=27
    MULTICOMMENT=28
    DIGIT=29
    WS=30

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
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.line()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 436011404) != 0)):
                    break

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
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 7, 8, 16, 18, 19, 20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.statement()
                self.state = 37
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 36
                    self.comment()


                pass
            elif token in [27, 28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
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
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.assignment()
                self.state = 43
                self.match(CParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.declaration()
                self.state = 46
                self.match(CParser.T__0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.logicexpression()
                self.state = 49
                self.match(CParser.T__0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.print_()
                self.state = 52
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
            self.state = 56
            self.match(CParser.T__1)
            self.state = 57
            self.match(CParser.T__2)
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.state = 58
                self.match(CParser.IDENTIFIER)
                pass
            elif token in [20, 21, 22, 23, 24]:
                self.state = 59
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 62
            self.match(CParser.T__3)
            self.state = 63
            self.match(CParser.T__0)
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
            self.state = 65
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
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
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 18, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.declaration()
                self.state = 68
                self.match(CParser.EQUALS)
                self.state = 69
                self.logicexpression()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.const_instantiation()
                self.state = 72
                self.match(CParser.EQUALS)
                self.state = 73
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


        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def POINTER(self):
            return self.getToken(CParser.POINTER, 0)

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
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.instantiation()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(CParser.IDENTIFIER)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.match(CParser.POINTER)
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

        def TYPE(self):
            return self.getToken(CParser.TYPE, 0)

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
            self.state = 82
            self.match(CParser.TYPE)
            self.state = 83
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

        def TYPE(self):
            return self.getToken(CParser.TYPE, 0)

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
            self.state = 85
            self.match(CParser.CONST)
            self.state = 86
            self.match(CParser.TYPE)
            self.state = 87
            self.match(CParser.IDENTIFIER)
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


        def LOGICOPS(self):
            return self.getToken(CParser.LOGICOPS, 0)

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
        self.enterRule(localctx, 18, self.RULE_logicexpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 89
                self.match(CParser.T__2)


            self.state = 92
            self.boolexpression()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 93
                self.match(CParser.LOGICOPS)
                self.state = 96
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 94
                    self.boolexpression()
                    pass

                elif la_ == 2:
                    self.state = 95
                    self.logicexpression()
                    pass




            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 100
                self.match(CParser.T__3)


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


        def COMPOPS(self):
            return self.getToken(CParser.COMPOPS, 0)

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
        self.enterRule(localctx, 20, self.RULE_boolexpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.term()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 104
                self.match(CParser.COMPOPS)
                self.state = 107
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 105
                    self.term()
                    pass

                elif la_ == 2:
                    self.state = 106
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


        def TERMOPS(self):
            return self.getToken(CParser.TERMOPS, 0)

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
        self.enterRule(localctx, 22, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.factor()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 112
                self.match(CParser.TERMOPS)
                self.state = 115
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 113
                    self.factor()
                    pass

                elif la_ == 2:
                    self.state = 114
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


        def FACTOROPS(self):
            return self.getToken(CParser.FACTOROPS, 0)

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
        self.enterRule(localctx, 24, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.element()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 120
                self.match(CParser.FACTOROPS)
                self.state = 123
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 121
                    self.element()
                    pass

                elif la_ == 2:
                    self.state = 122
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

        def literal(self):
            return self.getTypedRuleContext(CParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def POINTER(self):
            return self.getToken(CParser.POINTER, 0)

        def boolexpression(self):
            return self.getTypedRuleContext(CParser.BoolexpressionContext,0)


        def UNARYOPS(self):
            return self.getToken(CParser.UNARYOPS, 0)

        def SPECIALUNARY(self):
            return self.getToken(CParser.SPECIALUNARY, 0)

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
        self.enterRule(localctx, 26, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 127
                self.match(CParser.UNARYOPS)


            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 24]:
                self.state = 130
                self.literal()
                pass
            elif token in [19]:
                self.state = 131
                self.match(CParser.IDENTIFIER)
                pass
            elif token in [18]:
                self.state = 132
                self.match(CParser.POINTER)
                pass
            elif token in [3]:
                self.state = 133
                self.match(CParser.T__2)
                self.state = 134
                self.boolexpression()
                self.state = 135
                self.match(CParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 139
                self.match(CParser.SPECIALUNARY)


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

        def STRINGLITERAL(self):
            return self.getToken(CParser.STRINGLITERAL, 0)

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
        self.enterRule(localctx, 28, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32505856) != 0)):
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





