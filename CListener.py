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


    # Enter a parse tree produced by CParser#expression.
    def enterExpression(self, ctx:CParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CParser#expression.
    def exitExpression(self, ctx:CParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CParser#compexpression.
    def enterCompexpression(self, ctx:CParser.CompexpressionContext):
        pass

    # Exit a parse tree produced by CParser#compexpression.
    def exitCompexpression(self, ctx:CParser.CompexpressionContext):
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



del CParser