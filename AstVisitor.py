from CVisitor import *
from CParser import *
from Nodes import *


class AstVisitor(CVisitor):
    def visitRun(self, ctx: CParser.RunContext):
        node = RunNode()
        lines = ctx.line()
        for line in lines:
            node.children.append(self.visitLine(line))
        return node

    def visitLine(self, ctx: CParser.LineContext):
        node = LineNode()
        node.children = []
        if ctx.statement():
            node.statement = self.visitStatement(ctx.statement())
            node.children.append(node.statement)
        if ctx.comment():
            node.comment = self.visitComment(ctx.comment())
            node.children.append(node.comment)
        return node

    def visitComment(self, ctx: CParser.CommentContext):
        node = CommentNode()
        node.children = []
        node.text = ctx.getText()
        return node

    def visitStatement(self, ctx: CParser.StatementContext):
        node = StatementNode()
        node.children = []
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

    def visitAssignment(self, ctx: CParser.AssignmentContext):
        node = AssignmentNode()
        node.children = []
        node.declaration = self.visitDeclaration(ctx.declaration())
        node.expression = self.visitBoolexpression(ctx.boolexpression())
        node.children = [node.declaration, node.expression]
        return node

    def visitDeclaration(self, ctx: CParser.DeclarationContext):
        node = None
        if ctx.instantiation():
            node = self.visitInstantiation(ctx.instantiation())
        elif ctx.IDENTIFIER():
            node = VariableNode()
            node.name = ctx.getText()
        elif ctx.POINTER():
            node = PointerNode()
            node.name = ctx.getText()
        node.children = []
        return node

    def visitInstantiation(self, ctx: CParser.InstantiationContext):
        node = InstantiationNode()
        node.children = []
        if ctx.CONST():
            node.const = True
        node.varType = ctx.TYPE()
        node.name = ctx.IDENTIFIER()
        return node

    def visitBoolexpression(self, ctx: CParser.BoolexpressionContext):
        if not ctx.BOOLOPS():
            return self.visitTerm(ctx.term(0))
        node = CompareNode()
        node.children = []
        node.operation = ctx.BOOLOPS()
        a = ctx.term(0)
        node.left = self.visitTerm(a)
        if ctx.boolexpression():
            node.right = self.visitBoolexpression(ctx.boolexpression())
        else:
            node.right = self.visitTerm(ctx.term(1))
        node.children = [node.left, node.right]
        return node

    def visitTerm(self, ctx: CParser.TermContext):
        if not ctx.TERMOPS():
            return self.visitFactor(ctx.factor(0))
        node = TermNode()
        node.children = []
        node.operation = ctx.TERMOPS()
        node.left = self.visitFactor(ctx.factor(0))
        if ctx.term():
            node.right = self.visitTerm(ctx.term())
        else:
            node.right = self.visitFactor(ctx.factor(1))
        node.children = [node.left, node.right]
        return node

    def visitFactor(self, ctx: CParser.FactorContext):
        if not ctx.FACTOROPS():
            return self.visitElement(ctx.element(0))
        node = FactorNode()
        node.children = []
        node.operation = ctx.FACTOROPS()
        node.left = self.visitElement(ctx.element(0))
        if ctx.factor():
            node.right = self.visitFactor(ctx.factor())
        else:
            node.right = self.visitElement(ctx.element(1))
        node.children = [node.left, node.right]
        return node

    def visitElement(self, ctx: CParser.ElementContext):
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
            node.operation = ctx.UNARYOPS()
            node.variable = SpecialUnaryNode()
            node.variable.type = ctx.SPECIALUNARY()
            node.variable.variable = variable
        elif ctx.UNARYOPS():
            node = UnaryNode()
            node.operation = ctx.UNARYOPS()
            node.variable = variable
        elif ctx.SPECIALUNARY():
            node = SpecialUnaryNode()
            node.operation = ctx.SPECIALUNARY()
            node.variable = variable
        else:
            return variable
        return node

    def visitLiteral(self, ctx: CParser.LiteralContext):
        node = LiteralNode()
        node.value = ctx.getText()
        if ctx.BOOLLITERAL():
            node.literalType = 'bool'
        elif ctx.INTLITERAL():
            node.literalType = 'int'
        elif ctx.FLOATLITERAL():
            node.literalType = 'float'
        elif ctx.CHARLITERAL():
            node.literalType = 'char'
        elif ctx.STRINGLITERAL():
            node.literalType = 'string'
        return node
