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

    # def visitChildren(self, node):
    #     result = None
    #     n = node.getChildCount()
    #     for i in range(n):
    #         c = node.getChild(i)
    #         result = c.accept(self)
    #     return result

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
            node.children = [self.visitDeclaration(ctx.declaration())]
        elif ctx.boolexpression():
            node.children = [self.visitBoolexpression(ctx.boolexpression())]
        else:
            node.children = [ctx.getText()]
        return node

    def visitAssignment(self, ctx:CParser.AssignmentContext):
        node = AssignmentNode()
        # node.children = self.visitChildrenList(ctx)
        node.declaration = self.visitDeclaration(ctx.declaration())
        node.expression = self.visitBoolexpression(ctx.boolexpression())
        return node

    def visitDeclaration(self, ctx:CParser.DeclarationContext):
        node = None
        if ctx.instantiation():
            node = self.visitInstantiation(ctx.instantiation())
        elif ctx.IDENTIFIER():
            node = VariableNode()
            node.name = ctx.getText()
        elif ctx.POINTER():
            node = PointerNode()
            node.name = ctx.getText()
        return node

    def visitInstantiation(self, ctx:CParser.InstantiationContext):
        node = InstantiationNode()
        if ctx.CONST():
            node.const = True
        node.type = ctx.TYPE()
        node.name = ctx.IDENTIFIER()
        return node

    def visitBoolexpression(self, ctx:CParser.BoolexpressionContext):
        if not ctx.BOOLOPS():
            return self.visitTerm(ctx.term(0))
        node = CompareNode()
        node.type = ctx.BOOLOPS()
        a = ctx.term(0)
        node.left = self.visitTerm(a)
        if ctx.boolexpression():
            node.right = self.visitBoolexpression(ctx.boolexpression())
        else:
            node.right = self.visitTerm(ctx.term(1))
        return node

    def visitTerm(self, ctx:CParser.TermContext):
        if not ctx.TERMOPS():
            return self.visitFactor(ctx.factor(0))
        node = TermNode()
        node.type = ctx.TERMOPS()
        node.left = self.visitFactor(ctx.factor(0))
        if ctx.term():
            node.right = self.visitTerm(ctx.term())
        else:
            node.right = self.visitFactor(ctx.factor(1))
        return node

    def visitFactor(self, ctx:CParser.FactorContext):
        if not ctx.FACTOROPS():
            return self.visitElement(ctx.element(0))
        node = FactorNode()
        node.type = ctx.FACTOROPS()
        node.left = self.visitElement(ctx.element(0))
        if ctx.factor():
            node.right = self.visitFactor(ctx.factor())
        else:
            node.right = self.visitElement(ctx.element(1))
        return node

    def visitElement(self, ctx:CParser.ElementContext):
        variable = None
        if ctx.literal():
            variable = self.visitLiteral(ctx.literal())
        elif ctx.IDENTIFIER():
            variable = VariableNode()
            variable.name = ctx.IDENTIFIER()
        elif ctx.POINTER():
            variable = PointerNode()
            variable.name = ctx.POINTER()
        elif ctx.boolexpression():
            variable = self.visitBoolexpression(ctx.boolexpression())
        node = None
        if ctx.UNARYOPS() and ctx.SPECIALUNARY():
            node = UnaryNode()
            node.type = ctx.UNARYOPS()
            node.variable = SpecialUnaryNode()
            node.variable.type = ctx.SPECIALUNARY()
            node.variable.variable = variable
        elif ctx.UNARYOPS():
            node = UnaryNode()
            node.type = ctx.UNARYOPS()
            node.variable = variable
        elif ctx.SPECIALUNARY():
            node = SpecialUnaryNode()
            node.type = ctx.SPECIALUNARY()
            node.variable = variable
        else:
            return variable
        return node

    def visitLiteral(self, ctx:CParser.LiteralContext):
        node = LiteralNode()
        node.value = ctx.getText()
        return node
