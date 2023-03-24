from CVisitor import *
from CParser import *
from Nodes import *


class AstVisitor(CVisitor):
    def visitChildrenList(self, node):
        result = []
        n = node.getChildCount()
        for i in range(n):
            c = node.getChild(i)
            result.append(c.accept(self))
        return result

    def visitChildren(self, node):
        result = None
        n = node.getChildCount()
        for i in range(n):
            c = node.getChild(i)
            result = c.accept(self)
        return result

    def visitRun(self, ctx:CParser.RunContext):
        node = RunNode()
        node.children = self.visitChildrenList(ctx)
        return node

    def visitLine(self, ctx:CParser.LineContext):
        node = LineNode()
        if ctx.statement():
            node.statement = self.visitStatement(ctx.statement())
        if ctx.comment():
            node.comment = self.visitComment(ctx.comment())
        return node

    def visitComment(self, ctx:CParser.CommentContext):
        node = CommentNode()
        node.text = ctx.getText()
        return node

    def visitStatement(self, ctx:CParser.StatementContext):
        node = StatementNode()
        node.instruction = ctx.getText()
        if ctx.assignment():
            node.children = [self.visitAssignment(ctx.assignment())]
        elif ctx.declaration():
            node.children = [self.visitAssignment(ctx.declaration())]
        elif ctx.expression():
            node.children = [self.visitAssignment(ctx.expression())]
        else:
            node.children = [ctx.getText()]
        return node

    def visitAssignment(self, ctx:CParser.AssignmentContext):
        node = AssignmentNode()
        node.declaration = self.visitChildrenList(ctx)
        return node

    def visitDeclaration(self, ctx:CParser.DeclarationContext):
        node = DeclarationNode()
        if ctx.instantiation():
            node.children = self.visitInstantiation(ctx.instantiation())
            return node
        node.name = ctx.getText()
        return node

    def visitInstantiation(self, ctx:CParser.InstantiationContext):
        node = InstantiationNode()
        if ctx.CONST():
            node.const = True
        node.type = ctx.TYPE()
        node.name = ctx.IDENTIFIER()
        return node

    def visitExpression(self, ctx:CParser.ExpressionContext):
        return self.visitChildrenList(ctx)

    def visitCompexpression(self, ctx:CParser.CompexpressionContext):
        node = CompareNode()
        if ctx.COMPOPS():
            node.comparison = ctx.COMPOPS()
        else:
            node.comparison = ctx.LOGICOPS()
        node.children = self.visitChildrenList(ctx)
        return node

    def visitTerm(self, ctx:CParser.TermContext):
        node = TermNode()
        node.operatin = ctx.TERMOPS()
        return node

    def visitFactor(self, ctx:CParser.FactorContext):
        return self.visitChildrenList(ctx)

    def visitElement(self, ctx:CParser.ElementContext):
        return "hey"