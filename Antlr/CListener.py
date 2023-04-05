# Generated from C.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete listener for a parse tree produced by CParser.
class CListener(ParseTreeListener):

    # Enter a parse tree produced by CParser#run.
    def enterRun(self, ctx:CParser.RunContext):
        pass

    # Exit a parse tree produced by CParser#run.
    def exitRun(self, ctx:CParser.RunContext):
        pass


    # Enter a parse tree produced by CParser#line.
    def enterLine(self, ctx:CParser.LineContext):
        pass

    # Exit a parse tree produced by CParser#line.
    def exitLine(self, ctx:CParser.LineContext):
        pass


    # Enter a parse tree produced by CParser#statement.
    def enterStatement(self, ctx:CParser.StatementContext):
        pass

    # Exit a parse tree produced by CParser#statement.
    def exitStatement(self, ctx:CParser.StatementContext):
        pass


    # Enter a parse tree produced by CParser#print.
    def enterPrint(self, ctx:CParser.PrintContext):
        pass

    # Exit a parse tree produced by CParser#print.
    def exitPrint(self, ctx:CParser.PrintContext):
        pass


    # Enter a parse tree produced by CParser#comment.
    def enterComment(self, ctx:CParser.CommentContext):
        pass

    # Exit a parse tree produced by CParser#comment.
    def exitComment(self, ctx:CParser.CommentContext):
        pass


    # Enter a parse tree produced by CParser#assignment.
    def enterAssignment(self, ctx:CParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CParser#assignment.
    def exitAssignment(self, ctx:CParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CParser#declaration.
    def enterDeclaration(self, ctx:CParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CParser#declaration.
    def exitDeclaration(self, ctx:CParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CParser#instantiation.
    def enterInstantiation(self, ctx:CParser.InstantiationContext):
        pass

    # Exit a parse tree produced by CParser#instantiation.
    def exitInstantiation(self, ctx:CParser.InstantiationContext):
        pass


    # Enter a parse tree produced by CParser#const_instantiation.
    def enterConst_instantiation(self, ctx:CParser.Const_instantiationContext):
        pass

    # Exit a parse tree produced by CParser#const_instantiation.
    def exitConst_instantiation(self, ctx:CParser.Const_instantiationContext):
        pass


    # Enter a parse tree produced by CParser#logicexpression.
    def enterLogicexpression(self, ctx:CParser.LogicexpressionContext):
        pass

    # Exit a parse tree produced by CParser#logicexpression.
    def exitLogicexpression(self, ctx:CParser.LogicexpressionContext):
        pass


    # Enter a parse tree produced by CParser#boolexpression.
    def enterBoolexpression(self, ctx:CParser.BoolexpressionContext):
        pass

    # Exit a parse tree produced by CParser#boolexpression.
    def exitBoolexpression(self, ctx:CParser.BoolexpressionContext):
        pass


    # Enter a parse tree produced by CParser#term.
    def enterTerm(self, ctx:CParser.TermContext):
        pass

    # Exit a parse tree produced by CParser#term.
    def exitTerm(self, ctx:CParser.TermContext):
        pass


    # Enter a parse tree produced by CParser#factor.
    def enterFactor(self, ctx:CParser.FactorContext):
        pass

    # Exit a parse tree produced by CParser#factor.
    def exitFactor(self, ctx:CParser.FactorContext):
        pass


    # Enter a parse tree produced by CParser#element.
    def enterElement(self, ctx:CParser.ElementContext):
        pass

    # Exit a parse tree produced by CParser#element.
    def exitElement(self, ctx:CParser.ElementContext):
        pass


    # Enter a parse tree produced by CParser#literal.
    def enterLiteral(self, ctx:CParser.LiteralContext):
        pass

    # Exit a parse tree produced by CParser#literal.
    def exitLiteral(self, ctx:CParser.LiteralContext):
        pass



del CParser