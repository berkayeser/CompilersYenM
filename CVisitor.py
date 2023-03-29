# Generated from C.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CParser import CParser
else:
    from CParser import CParser

# This class defines a complete generic visitor for a parse tree produced by CParser.

class CVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CParser#run.
    def visitRun(self, ctx:CParser.RunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#line.
    def visitLine(self, ctx:CParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#statement.
    def visitStatement(self, ctx:CParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#comment.
    def visitComment(self, ctx:CParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#assignment.
    def visitAssignment(self, ctx:CParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declaration.
    def visitDeclaration(self, ctx:CParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#instantiation.
    def visitInstantiation(self, ctx:CParser.InstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#logicexpression.
    def visitLogicexpression(self, ctx:CParser.LogicexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#boolexpression.
    def visitBoolexpression(self, ctx:CParser.BoolexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#term.
    def visitTerm(self, ctx:CParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#factor.
    def visitFactor(self, ctx:CParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#element.
    def visitElement(self, ctx:CParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#literal.
    def visitLiteral(self, ctx:CParser.LiteralContext):
        return self.visitChildren(ctx)



del CParser