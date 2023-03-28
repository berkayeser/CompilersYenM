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
        4,1,31,120,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,1,1,1,3,1,32,8,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,50,8,2,1,2,1,2,3,2,54,8,2,1,
        3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,3,5,65,8,5,1,6,3,6,68,8,6,1,6,
        1,6,1,6,1,7,3,7,74,8,7,1,7,1,7,1,7,1,7,3,7,80,8,7,3,7,82,8,7,1,7,
        3,7,85,8,7,1,8,1,8,1,8,1,8,3,8,91,8,8,3,8,93,8,8,1,9,1,9,1,9,1,9,
        3,9,99,8,9,3,9,101,8,9,1,10,3,10,104,8,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,3,10,113,8,10,1,10,3,10,116,8,10,1,11,1,11,1,11,0,0,
        12,0,2,4,6,8,10,12,14,16,18,20,22,0,2,1,0,28,29,1,0,21,25,130,0,
        25,1,0,0,0,2,34,1,0,0,0,4,53,1,0,0,0,6,55,1,0,0,0,8,57,1,0,0,0,10,
        64,1,0,0,0,12,67,1,0,0,0,14,73,1,0,0,0,16,86,1,0,0,0,18,94,1,0,0,
        0,20,103,1,0,0,0,22,117,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,1,1,0,0,0,29,31,3,4,2,0,30,
        32,3,6,3,0,31,30,1,0,0,0,31,32,1,0,0,0,32,35,1,0,0,0,33,35,3,6,3,
        0,34,29,1,0,0,0,34,33,1,0,0,0,35,3,1,0,0,0,36,37,3,8,4,0,37,38,5,
        1,0,0,38,54,1,0,0,0,39,40,3,10,5,0,40,41,5,1,0,0,41,54,1,0,0,0,42,
        43,3,14,7,0,43,44,5,1,0,0,44,54,1,0,0,0,45,46,5,2,0,0,46,49,5,3,
        0,0,47,50,5,20,0,0,48,50,3,22,11,0,49,47,1,0,0,0,49,48,1,0,0,0,50,
        51,1,0,0,0,51,52,5,4,0,0,52,54,5,1,0,0,53,36,1,0,0,0,53,39,1,0,0,
        0,53,42,1,0,0,0,53,45,1,0,0,0,54,5,1,0,0,0,55,56,7,0,0,0,56,7,1,
        0,0,0,57,58,3,10,5,0,58,59,5,18,0,0,59,60,3,14,7,0,60,9,1,0,0,0,
        61,65,3,12,6,0,62,65,5,20,0,0,63,65,5,19,0,0,64,61,1,0,0,0,64,62,
        1,0,0,0,64,63,1,0,0,0,65,11,1,0,0,0,66,68,5,17,0,0,67,66,1,0,0,0,
        67,68,1,0,0,0,68,69,1,0,0,0,69,70,5,8,0,0,70,71,5,20,0,0,71,13,1,
        0,0,0,72,74,5,3,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,
        81,3,16,8,0,76,79,5,5,0,0,77,80,3,16,8,0,78,80,3,14,7,0,79,77,1,
        0,0,0,79,78,1,0,0,0,80,82,1,0,0,0,81,76,1,0,0,0,81,82,1,0,0,0,82,
        84,1,0,0,0,83,85,5,4,0,0,84,83,1,0,0,0,84,85,1,0,0,0,85,15,1,0,0,
        0,86,92,3,18,9,0,87,90,5,10,0,0,88,91,3,18,9,0,89,91,3,16,8,0,90,
        88,1,0,0,0,90,89,1,0,0,0,91,93,1,0,0,0,92,87,1,0,0,0,92,93,1,0,0,
        0,93,17,1,0,0,0,94,100,3,20,10,0,95,98,5,11,0,0,96,99,3,20,10,0,
        97,99,3,18,9,0,98,96,1,0,0,0,98,97,1,0,0,0,99,101,1,0,0,0,100,95,
        1,0,0,0,100,101,1,0,0,0,101,19,1,0,0,0,102,104,5,9,0,0,103,102,1,
        0,0,0,103,104,1,0,0,0,104,112,1,0,0,0,105,113,3,22,11,0,106,113,
        5,20,0,0,107,113,5,19,0,0,108,109,5,3,0,0,109,110,3,14,7,0,110,111,
        5,4,0,0,111,113,1,0,0,0,112,105,1,0,0,0,112,106,1,0,0,0,112,107,
        1,0,0,0,112,108,1,0,0,0,113,115,1,0,0,0,114,116,5,12,0,0,115,114,
        1,0,0,0,115,116,1,0,0,0,116,21,1,0,0,0,117,118,7,1,0,0,118,23,1,
        0,0,0,18,27,31,34,49,53,64,67,73,79,81,84,90,92,98,100,103,112,115
    ]

class CParser ( Parser ):

    grammarFileName = "C.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'printf'", "'('", "')'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'int'", "'char'", 
                     "'bool'", "'float'", "'const'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOLOPS", "COMPOPS", "LOGICOPS", "TYPE", 
                      "UNARYOPS", "TERMOPS", "FACTOROPS", "SPECIALUNARY", 
                      "INT", "CHAR", "BOOL", "FLOAT", "CONST", "EQUALS", 
                      "POINTER", "IDENTIFIER", "INTLITERAL", "FLOATLITERAL", 
                      "BOOLLITERAL", "CHARLITERAL", "STRINGLITERAL", "SINGLESTRING", 
                      "DOUBLESTRING", "SINGLECOMMENT", "MULTICOMMENT", "DIGIT", 
                      "WS" ]

    RULE_run = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_comment = 3
    RULE_assignment = 4
    RULE_declaration = 5
    RULE_instantiation = 6
    RULE_boolexpression = 7
    RULE_term = 8
    RULE_factor = 9
    RULE_element = 10
    RULE_literal = 11

    ruleNames =  [ "run", "line", "statement", "comment", "assignment", 
                   "declaration", "instantiation", "boolexpression", "term", 
                   "factor", "element", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    BOOLOPS=5
    COMPOPS=6
    LOGICOPS=7
    TYPE=8
    UNARYOPS=9
    TERMOPS=10
    FACTOROPS=11
    SPECIALUNARY=12
    INT=13
    CHAR=14
    BOOL=15
    FLOAT=16
    CONST=17
    EQUALS=18
    POINTER=19
    IDENTIFIER=20
    INTLITERAL=21
    FLOATLITERAL=22
    BOOLLITERAL=23
    CHARLITERAL=24
    STRINGLITERAL=25
    SINGLESTRING=26
    DOUBLESTRING=27
    SINGLECOMMENT=28
    MULTICOMMENT=29
    DIGIT=30
    WS=31

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
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.line()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 872022796) != 0)):
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
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 8, 9, 17, 19, 20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.statement()
                self.state = 31
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.comment()


                pass
            elif token in [28, 29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
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


        def boolexpression(self):
            return self.getTypedRuleContext(CParser.BoolexpressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(CParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(CParser.LiteralContext,0)


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
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.assignment()
                self.state = 37
                self.match(CParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.declaration()
                self.state = 40
                self.match(CParser.T__0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.boolexpression()
                self.state = 43
                self.match(CParser.T__0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(CParser.T__1)
                self.state = 46
                self.match(CParser.T__2)
                self.state = 49
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [20]:
                    self.state = 47
                    self.match(CParser.IDENTIFIER)
                    pass
                elif token in [21, 22, 23, 24, 25]:
                    self.state = 48
                    self.literal()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 51
                self.match(CParser.T__3)
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
        self.enterRule(localctx, 6, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
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

        def boolexpression(self):
            return self.getTypedRuleContext(CParser.BoolexpressionContext,0)


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
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.declaration()
            self.state = 58
            self.match(CParser.EQUALS)
            self.state = 59
            self.boolexpression()
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
        self.enterRule(localctx, 10, self.RULE_declaration)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.instantiation()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(CParser.IDENTIFIER)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
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

        def CONST(self):
            return self.getToken(CParser.CONST, 0)

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
        self.enterRule(localctx, 12, self.RULE_instantiation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 66
                self.match(CParser.CONST)


            self.state = 69
            self.match(CParser.TYPE)
            self.state = 70
            self.match(CParser.IDENTIFIER)
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


        def BOOLOPS(self):
            return self.getToken(CParser.BOOLOPS, 0)

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
        self.enterRule(localctx, 14, self.RULE_boolexpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 72
                self.match(CParser.T__2)


            self.state = 75
            self.term()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 76
                self.match(CParser.BOOLOPS)
                self.state = 79
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 77
                    self.term()
                    pass

                elif la_ == 2:
                    self.state = 78
                    self.boolexpression()
                    pass




            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 83
                self.match(CParser.T__3)


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
        self.enterRule(localctx, 16, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.factor()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 87
                self.match(CParser.TERMOPS)
                self.state = 90
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 88
                    self.factor()
                    pass

                elif la_ == 2:
                    self.state = 89
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
        self.enterRule(localctx, 18, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.element()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 95
                self.match(CParser.FACTOROPS)
                self.state = 98
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 96
                    self.element()
                    pass

                elif la_ == 2:
                    self.state = 97
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
        self.enterRule(localctx, 20, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 102
                self.match(CParser.UNARYOPS)


            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 22, 23, 24, 25]:
                self.state = 105
                self.literal()
                pass
            elif token in [20]:
                self.state = 106
                self.match(CParser.IDENTIFIER)
                pass
            elif token in [19]:
                self.state = 107
                self.match(CParser.POINTER)
                pass
            elif token in [3]:
                self.state = 108
                self.match(CParser.T__2)
                self.state = 109
                self.boolexpression()
                self.state = 110
                self.match(CParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 114
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
        self.enterRule(localctx, 22, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65011712) != 0)):
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





