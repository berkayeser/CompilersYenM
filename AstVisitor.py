from Antlr.CVisitor import *
from Antlr.CParser import *
from Nodes import *
from AST import AST
from SymboolTabel import SymboolTabel


class AstVisitor(CVisitor):
    def __init__(self):
        self.symbol_table = SymboolTabel()

    def visitRun(self, ctx: CParser.RunContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        ast = AST()
        node = RunNode()
        lines = ctx.line()
        for line in lines:
            node.children.append(self.visitLine(line))
        ast.root = node
        return ast

    def visitLine(self, ctx: CParser.LineContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        node = LineNode()
        if ctx.statement():
            node.statement = self.visitStatement(ctx.statement())
            node.children.append(node.statement)
        if ctx.comment():
            node.comment = self.visitComment(ctx.comment())
            node.children.append(node.comment)
        return node

    def visitStatement(self, ctx: CParser.StatementContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
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

    def visitPrint(self, ctx: CParser.PrintContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        node = PrintNode()
        if ctx.literal():
            node.toPrint = ctx.literal().__str__()
        elif ctx.IDENTIFIER():
            node.toPrint = ctx.IDENTIFIER().__str__()
        return node

    def visitComment(self, ctx: CParser.CommentContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        node = CommentNode()
        node.text = ctx.getText()
        return node

    def visitAssignment(self, ctx: CParser.AssignmentContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
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
        if ctx.exception is not None:
            raise Exception("syntax error")
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
        elif ctx.pointer():
            node = self.visitPointer(ctx.pointer())
        return node

    def visitInstantiation(self, ctx: CParser.InstantiationContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        node = InstantiationNode()
        node.const = False
        node.name = ctx.IDENTIFIER().__str__()
        node.varType = self.visitType(ctx.type_())
        # (Checking for) Redeclaration or redefinition of an existing variable
        self.symbol_table.add_symbol(str(node.name), str(node.varType))

        return node

    def visitConst_instantiation(self, ctx: CParser.Const_instantiationContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        node = InstantiationNode()
        node.const = True
        node.name = ctx.IDENTIFIER().__str__()
        node.varType = self.visitType(ctx.type_())
        # (Checking for) Redeclaration or redefinition of an existing variable
        self.symbol_table.add_symbol(str(node.name), "const"+str(node.varType))

        return node

    def visitType(self, ctx: CParser.TypeContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        return ctx.getText()

    def visitLogicexpression(self, ctx: CParser.LogicexpressionContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        if not ctx.logicops():
            a = ctx.boolexpression()
            b = ctx.boolexpression(0)
            return self.visitBoolexpression(ctx.boolexpression(0))
        node = LogicNode()
        node.operation = ctx.logicops().getText()
        node.left = self.visitBoolexpression(ctx.boolexpression(0))
        if ctx.logicexpression():
            node.right = self.visitLogicexpression(ctx.logicexpression())
        else:
            node.right = self.visitBoolexpression(ctx.boolexpression(1))
        node.children = [node.left, node.right]
        return node

    def visitBoolexpression(self, ctx: CParser.BoolexpressionContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        if not ctx.compops():
            return self.visitTerm(ctx.term(0))
        if not ctx.boolexpression():
            node = CompareNode()
            node.operation = ctx.compops().getText()
            node.left = self.visitTerm(ctx.term(0))
            node.right = self.visitTerm(ctx.term(1))
            node.children = [node.left, node.right]
            return node
        node = LogicNode()
        node.operation = "&&"
        compNode1 = CompareNode()
        compNode1.operation = ctx.compops().getText()
        compNode2 = self.visitBoolexpression(ctx.boolexpression())
        compNode1.left = self.visitTerm(ctx.term(0))
        compNode1.right = compNode2.left
        node.left = compNode1
        node.right = compNode2
        node.children = [node.left, node.right]
        return node

    def visitTerm(self, ctx: CParser.TermContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        if not ctx.termops():
            return self.visitFactor(ctx.factor(0))
        node = TermNode()
        node.operation = ctx.termops().getText()
        node.left = self.visitFactor(ctx.factor(0))
        if ctx.term():
            node.right = self.visitTerm(ctx.term())
        else:
            node.right = self.visitFactor(ctx.factor(1))
        node.children = [node.left, node.right]
        return node

    def visitFactor(self, ctx: CParser.FactorContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        if not ctx.factorops():
            return self.visitElement(ctx.element(0))
        node = FactorNode()
        node.operation = ctx.factorops().getText()
        node.left = self.visitElement(ctx.element(0))
        if ctx.factor():
            node.right = self.visitFactor(ctx.factor())
        else:
            node.right = self.visitElement(ctx.element(1))
        node.children = [node.left, node.right]
        return node

    def visitElement(self, ctx: CParser.ElementContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        node = None
        variable = None
        if ctx.typecast():
            node = TypeCastNode()
            node.castTo = ctx.typecast().getText()[1:-1]
            node.variable = self.visitElement(ctx.element())
            node.children = [node.variable]
        elif ctx.unaryops():
            node = UnaryNode()
            node.operation = ctx.unaryops().getText()
            node.variable = self.visitElement(ctx.element())
            node.children = [node.variable]

        elif ctx.literal():
            node = self.visitLiteral(ctx.literal())
        elif ctx.pointer():
            node = self.visitPointer(ctx.pointer())
        elif ctx.IDENTIFIER():
            node = VariableNode()
            node.name = ctx.IDENTIFIER().__str__()
            # Use of an uninitialized variable
            self.symbol_table.get_symbol(str(node.name), "unint")
        elif ctx.boolexpression():
            node = self.visitBoolexpression(ctx.boolexpression())
        if ctx.SPECIALUNARY():
            newNode = SpecialUnaryNode()
            newNode.operation = ctx.SPECIALUNARY().__str__()
            newNode.variable = node
            newNode.children = [newNode.variable]
            node = newNode
        return node

    def visitPointer(self, ctx: CParser.PointerContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        node = UnaryNode()
        node.operation = ctx.STAR().__str__()
        variable = None
        if ctx.IDENTIFIER():
            variable = VariableNode()
            variable.name = ctx.IDENTIFIER().__str__()
            # Use of an uninitialized variable
            self.symbol_table.get_symbol(str(variable.name), "unint")
        elif ctx.pointer():
            variable = self.visitPointer(ctx.pointer())
        node.variable = variable
        return node

    def visitLiteral(self, ctx: CParser.LiteralContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
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
