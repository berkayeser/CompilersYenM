# Generated from Antlr/C.g4 by ANTLR 4.12.0
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


    # Visit a parse tree produced by CParser#print.
    def visitPrint(self, ctx:CParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#comment.
    def visitComment(self, ctx:CParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#assignment.
    def visitAssignment(self, ctx:CParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#rvalue_assignment.
    def visitRvalue_assignment(self, ctx:CParser.Rvalue_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#declaration.
    def visitDeclaration(self, ctx:CParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#instantiation.
    def visitInstantiation(self, ctx:CParser.InstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#const_instantiation.
    def visitConst_instantiation(self, ctx:CParser.Const_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#type.
    def visitType(self, ctx:CParser.TypeContext):
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


    # Visit a parse tree produced by CParser#logicops.
    def visitLogicops(self, ctx:CParser.LogicopsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#compops.
    def visitCompops(self, ctx:CParser.CompopsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#termops.
    def visitTermops(self, ctx:CParser.TermopsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#factorops.
    def visitFactorops(self, ctx:CParser.FactoropsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#unaryops.
    def visitUnaryops(self, ctx:CParser.UnaryopsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#typecast.
    def visitTypecast(self, ctx:CParser.TypecastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#pointer.
    def visitPointer(self, ctx:CParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CParser#literal.
    def visitLiteral(self, ctx:CParser.LiteralContext):
        return self.visitChildren(ctx)



del CParser