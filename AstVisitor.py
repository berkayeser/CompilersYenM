from Antlr.CVisitor import *
from Antlr.CParser import *
from Nodes import *
from AST import AST
from SymboolTabel import SymboolTabel


class AstVisitor(CVisitor):
    def __init__(self):
        self.symbol_table = SymboolTabel()

    def visitRun(self, ctx: CParser.RunContext):
        ast = AST()
        node = RunNode()
        lines = ctx.line()
        for line in lines:
            node.children.append(self.visitLine(line))
        ast.root = node
        return ast

    def visitLine(self, ctx: CParser.LineContext):
        node = LineNode()
        if ctx.statement():
            node.statement = self.visitStatement(ctx.statement())
            node.children.append(node.statement)
        if ctx.comment():
            node.comment = self.visitComment(ctx.comment())
            node.children.append(node.comment)
        return node

    def visitPrint(self, ctx: CParser.PrintContext):
        node = PrintNode()
        if ctx.literal():
            node.toPrint = ctx.literal().__str__()
        elif ctx.IDENTIFIER():
            node.toPrint = ctx.IDENTIFIER().__str__()
        return node

    def visitComment(self, ctx: CParser.CommentContext):
        node = CommentNode()
        node.text = ctx.getText()
        return node

    def visitStatement(self, ctx: CParser.StatementContext):
        node = StatementNode()
        node.instruction = ctx.getText()
        if ctx.assignment():
            node.children = [self.visitAssignment(ctx.assignment())]
        elif ctx.declaration():
            node.children = [self.visitDeclaration(ctx.declaration())]
        elif ctx.logicexpression():
            node.children = [self.visitLogicexpression(ctx.logicexpression())]
        elif ctx.print_():
            node.children = [self.visitPrint(ctx.print_())]
        else:
            node.children = [ctx.getText()]
        return node

    def visitAssignment(self, ctx: CParser.AssignmentContext):
        node = AssignmentNode()
        if ctx.declaration():
            node.left = self.visitDeclaration(ctx.declaration())
        elif ctx.const_instantiation():
            node.left = self.visitConst_instantiation(ctx.const_instantiation())
        node.right = self.visitLogicexpression(ctx.logicexpression())
        node.children = [node.left, node.right]

        # Operations of incompatible types "inta;floatb;a=b;" zie BB

        # Assignments of incompatible types "inta=1;floatb=a;" OF "inta;floatb;a=b;"
        # bv "int a; float b; a=b;"
        if node.left.type == "variable" and node.right.type == "variable":
            nodeLn = str(node.left.name)
            nodeRn = str(node.right.name)
            nodeLt = self.symbol_table.get_symbol(nodeLn)['type']
            nodeRt = self.symbol_table.get_symbol(nodeRn)['type']
            if nodeLt != nodeRt:
                raise Exception(f"Variable '{nodeRn}' of type '{nodeRt}' gets assigned to variable '{nodeLn}' of incompatible type '{nodeLt}'. ")

        # bv "int a = 1; float b = a;"
        if node.left.type == "instantiation" and node.right.type == "variable":
            nodeLn = str(node.left.name)
            nodeRn = str(node.right.name)
            nodeLt = str(node.left.varType)
            nodeRt = self.symbol_table.get_symbol(nodeRn)['type']

            if node.left.const:
                nodeLt = "const" + nodeLt

            if nodeLt != nodeRt:
                raise Exception(f"During definition, Variable '{nodeRn}' of type '{nodeRt}' gets assigned to variable '{nodeLn}' of incompatible type '{nodeLt}'. ")

        return node

    def visitDeclaration(self, ctx: CParser.DeclarationContext):
        node = None
        if ctx.instantiation():
            node = self.visitInstantiation(ctx.instantiation())
        elif ctx.IDENTIFIER(): # bv x:var = 3
            node = VariableNode()
            node.name = ctx.getText()

            # Use of an undefined variable
            type1 = self.symbol_table.get_symbol(str(node.name), "undef")['type']
            # Assignment to a const variable.
            if type1[0:5] == "const":
                raise Exception(f"Assignment to the const variable '{str(node.name)}' with type '{type1}'.")

        elif ctx.POINTER():
            node = PointerNode()
            node.name = ctx.getText()
        return node

    def visitInstantiation(self, ctx: CParser.InstantiationContext):
        node = InstantiationNode()
        node.const = False
        node.varType = ctx.TYPE().__str__()
        node.name = ctx.IDENTIFIER().__str__()

        # (Checking for) Redeclaration or redefinition of an existing variable
        self.symbol_table.add_symbol(str(node.name), str(node.varType))

        return node

    def visitConst_instantiation(self, ctx: CParser.Const_instantiationContext):
        node = InstantiationNode()
        node.const = True
        node.varType = ctx.TYPE().__str__()
        node.name = ctx.IDENTIFIER().__str__()

        # (Checking for) Redeclaration or redefinition of an existing variable
        self.symbol_table.add_symbol(str(node.name), "const"+str(node.varType))

        return node

    def visitLogicexpression(self, ctx: CParser.LogicexpressionContext):
        if not ctx.LOGICOPS():
            return self.visitBoolexpression(ctx.boolexpression(0))
        node = LogicNode()
        node.operation = ctx.LOGICOPS().__str__()
        a = ctx.boolexpression(0)
        node.left = self.visitBoolexpression(a)
        if ctx.logicexpression():
            node.right = self.visitLogicexpression(ctx.logicexpression())
        else:
            node.right = self.visitBoolexpression(ctx.boolexpression(1))
        node.children = [node.left, node.right]
        return node

    def visitBoolexpression(self, ctx: CParser.BoolexpressionContext):
        if not ctx.COMPOPS():
            return self.visitTerm(ctx.term(0))
        if not ctx.boolexpression():
            node = CompareNode()
            node.operation = ctx.COMPOPS().__str__()
            node.left = self.visitTerm(ctx.term(0))
            node.right = self.visitTerm(ctx.term(1))
            node.children = [node.left, node.right]
            return node
        node = LogicNode()
        node.operation = "&&"
        compNode1 = CompareNode()
        compNode1.operation = ctx.COMPOPS().__str__()
        compNode2 = self.visitBoolexpression(ctx.boolexpression())
        compNode1.left = self.visitTerm(ctx.term(0))
        compNode1.right = compNode2.left
        node.left = compNode1
        node.right = compNode2
        node.children = [node.left, node.right]
        return node

    def visitTerm(self, ctx: CParser.TermContext):
        if not ctx.TERMOPS():
            return self.visitFactor(ctx.factor(0))
        node = TermNode()
        node.operation = ctx.TERMOPS().__str__()
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
        node.operation = ctx.FACTOROPS().__str__()
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
        elif ctx.IDENTIFIER(): # ... = x: var
            variable = VariableNode()
            variable.name = ctx.IDENTIFIER()

            # Use of an uninitialized variable
            self.symbol_table.get_symbol(str(variable.name), "unint")
            variable.name = ctx.IDENTIFIER().__str__()
        elif ctx.POINTER():
            variable = PointerNode()
            variable.name = ctx.POINTER().__str__()
        elif ctx.boolexpression():
            variable = self.visitBoolexpression(ctx.boolexpression())
        node = None
        if ctx.UNARYOPS() and ctx.SPECIALUNARY():
            node = UnaryNode()
            node.operation = ctx.UNARYOPS().__str__()
            node.variable = SpecialUnaryNode()
            node.variable.type = ctx.SPECIALUNARY()
            node.variable.variable = variable
        elif ctx.UNARYOPS():
            node = UnaryNode()
            node.operation = ctx.UNARYOPS().__str__()
            node.variable = variable
        elif ctx.SPECIALUNARY():
            node = SpecialUnaryNode()
            node.operation = ctx.SPECIALUNARY().__str__()
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
        return node
