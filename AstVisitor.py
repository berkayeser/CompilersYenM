from Antlr.CVisitor import *
from Antlr.CParser import *
from Nodes import *
from AST import AST
from SymbolTable import SymbolTable


class AstVisitor(CVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()

    def visitRun(self, ctx: CParser.RunContext):
        if ctx.exception is not None:
            raise Exception("syntax error")

        ast = AST()
        node = RunNode()
        lines = ctx.line()
        for line in lines:
            temp = self.visitLine(line)
            if isinstance(temp, tuple):
                for t in temp:
                    node.children.append(t)
            else:
                if temp.type == "break" or temp.type == "continue":
                    break
                node.children.append(temp)
        ast.root = node
        return ast

    def visitBlock_scope(self, ctx: CParser.Block_scopeContext):
        if ctx.exception is not None:
            raise Exception("syntax error")
        node = BlockNode()
        nodes = []
        lines = ctx.line()
        self.symbol_table.open_scope()
        for line in lines:
            temp = self.visitLine(line)
            if isinstance(temp, tuple):
                for t in temp:
                    nodes.append(t)
            else:
                if temp.type == "break" or temp.type == "continue":
                    break
                nodes.append(temp)
        node.children = nodes
        self.symbol_table.close_scope()
        return node

    def visitLine(self, ctx: CParser.LineContext):
        if ctx.exception is not None:
            raise Exception("syntax error")

        line_nr = -1
        node = None
        if ctx.expression_statement():
            node = LineNode()
            node.statement = self.visitExpression_statement(ctx.expression_statement(), line_nr)
            node.children.append(node.statement)
        elif ctx.jump_statement():
            node = LineNode()
            node.statement = self.visitJump_statement(ctx.jump_statement())
            node.children.append(node.statement)
        elif ctx.compound_statement():
            node = self.visitCompound_statement(ctx.compound_statement(), line_nr)
        elif ctx.block_scope():
            node = BlockNode()
            node.block = self.visitBlock_scope(ctx.block_scope())
            node.children.append(node.block)
        if ctx.comment() and node is None:
            node = self.visitComment(ctx.comment())
        elif ctx.comment():
            node.comment = self.visitComment(ctx.comment())
            node.children.append(node.comment)
        return node

    def visitJump_statement(self, ctx: CParser.Jump_statementContext):
        if ctx.exception is not None:
            raise Exception("syntax error")

        if ctx.break_():
            return BreakNode()
        elif ctx.continue_():
            return ContinueNode()

    def visitCompound_statement(self, ctx: CParser.Compound_statementContext, line_nr:int=-1):
        if ctx.exception is not None:
            raise Exception("syntax error")

        node = None
        if ctx.if_():
            node = self.visitIf(ctx.if_())
        elif ctx.while_():
            node = self.visitWhile(ctx.while_())
        elif ctx.for_():
            node = self.visitFor(ctx.for_(), line_nr)
            isFor = True

        if node is None:
            raise Exception("Node is node")

        return node

    def visitIf(self, ctx: CParser.IfContext):
        if ctx.exception is not None:
            raise Exception("syntax error")

        node = IfNode()
        node.condition = self.visitCondition(ctx.condition())
        node.block = self.visitBlock_scope(ctx.block_scope())
        node.children = [node.condition, node.block]
        if ctx.else_():
            node.elseNode = self.visitElse(ctx.else_())
            node.children.append(node.elseNode)
        return node

    def visitCondition(self, ctx: CParser.ConditionContext):
        return self.visitLogicexpression(ctx.logicexpression())

    def visitElse(self, ctx: CParser.ElseContext):
        if ctx.exception is not None:
            raise Exception("syntax error")

        node = ElseNode()
        node.block = self.visitBlock_scope(ctx.block_scope())
        node.children = [node.block]
        return node

    def visitWhile(self, ctx: CParser.WhileContext):
        if ctx.exception is not None:
            raise Exception("syntax error")

        node = WhileNode()
        node.condition = self.visitCondition(ctx.condition())
        node.block = self.visitBlock_scope(ctx.block_scope())
        node.children = [node.condition, node.block]

        return node

    # returns two nodes instead of one
    def visitFor(self, ctx: CParser.ForContext, line_nr:int=-1):
        if ctx.exception is not None:
            raise Exception("syntax error")

        While_node = WhileNode()
        Line_node = LineNode()
        condition = self.visitFor_condition(ctx.for_condition(), line_nr)
        Line_node.statement = condition[0]
        While_node.condition = condition[1]
        While_node.block = self.visitBlock_scope(ctx.block_scope())
        While_node.block.children.insert(0, condition[2])
        Line_node.children = [Line_node.statement]
        While_node.children = [While_node.condition, While_node.block]

        return Line_node, While_node

    def visitFor_condition(self, ctx: CParser.For_conditionContext, line_nr:int = -1):
        if ctx.exception is not None:
            raise Exception("syntax error")

        condition = [self.visitAssignment(ctx.assignment(), line_nr), self.visitLogicexpression(ctx.logicexpression()),
                     self.visitUpdate_expression(ctx.update_expression())]

        return condition

    def visitUpdate_expression(self, ctx: CParser.Update_expressionContext):
        if ctx.EQUALS():
            node = AssignmentNode()
            if ctx.IDENTIFIER():
                node.left = VariableNode()
                node.left.name = ctx.getText()
            elif ctx.pointer():
                node.left = self.visitPointer(ctx.pointer())
            node.right = self.visitLogicexpression(ctx.logicexpression())
            node.children = [node.left, node.right]
        else:
            return self.visitLogicexpression(ctx.logicexpression())

    def visitExpression_statement(self, ctx: CParser.Expression_statementContext, line_nr:int = -1):
        if ctx.exception is not None:
            raise Exception("syntax error")

        node = ExpressionStatementNode()
        node.instruction = ctx.getText()
        if ctx.assignment():
            node.children = [self.visitAssignment(ctx.assignment(), line_nr)]
        elif ctx.declaration():
            node.children = [self.visitDeclaration(ctx.declaration(), line_nr)]
        elif ctx.logicexpression():
            node.children = [self.visitLogicexpression(ctx.logicexpression())]
        elif ctx.print_():
            node.children = [self.visitPrint(ctx.print_())]
        else:
            node.children = []
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

    def visitAssignment(self, ctx: CParser.AssignmentContext, line_nr:int = -1):
        if ctx.exception is not None:
            raise Exception("syntax error")
        if ctx.rvalue_assignment():
            raise Exception(f"cannot assign rvalue {ctx.rvalue_assignment().logicexpression(0).getText()}")
        node = AssignmentNode()
        if ctx.declaration():
            node.left = self.visitDeclaration(ctx.declaration(), line_nr)
        elif ctx.const_instantiation():
            node.left = self.visitConst_instantiation(ctx.const_instantiation())
        node.right = self.visitLogicexpression(ctx.logicexpression())
        node.children = [node.left, node.right]

        # Adding variable values to the symbol table
        if node.right.type == 'literal':
            if node.left.type in ['instantiation', 'variable']:
                # Als de waarde van dit symbool voorheen al ingevuld is, duiden we dit aan
                #if self.symbol_table.get_symbol(node.left.name)['value'] is not None:
                if self.symbol_table.symbol_used_current(node.left.name):
                    self.symbol_table.symbol_used_twice(node.left.name)
                else:
                    self.symbol_table.add_symbol_value(node.left.name, node.right.value)
            # else:  bv. nodelefttype = unary bv "*ptr = 2;"

        # Operations of incompatible types
        # int x = 2; int b = 3; const int * x_ptr = & x; *x_ptr = b;
        if node.left.type == "unary" and node.right.type == "variable":
            nlvn = node.left.variable.name
            nlvnt = self.symbol_table.get_symbol(nlvn)['type']
            if nlvnt[0:5] == "const":
                raise Exception(f"Semantic Error; Pointed value of '{nlvn}' of type '{nlvnt}' cannot be changed.")

        if node.right.type == "unary":

            if node.right.variable.type == "literal":
                nrvn = "literal"
                nrvt = node.right.variable.literalType
            elif node.right.variable.type == "variable":
                nrvn = node.right.variable.name
                nrvt = self.symbol_table.get_symbol(nrvn)['type']
            elif node.right.variable.type == "unary":
                nr = node.right.variable
                while nr.type == "unary":
                    nr = nr.variable
                # Nu is nr een variabele
                nrvn = nr.name
                nrvt = self.symbol_table.get_symbol(nrvn)['type']
            else:
                print("error")
                nrvt, nrvn = "error", "error"

            if node.right.operation == "*":
                if nrvt[-1] != '*':
                    raise Exception(f"Semantic Error; Can't dereference non-pointer '{nrvn}' of type '{nrvt}'.")
            elif node.right.operation == "&":
                # BV int b = 4; int** m = &b;
                nlvn = node.left.name
                nlvt = self.symbol_table.get_symbol(nlvn)['type']

                if nlvt[-2:] == "**":
                    if nrvt[-1] != "*":
                        raise Exception(
                            f"Semantic Error; Can't assign address of '{nrvn}' of type '{nrvt}' to '{nlvn}' of type '{nlvt}'.")

                def trim(word: str) -> str:
                    if word[:5] == "const":
                        word = word[5:]
                    if word[-2:] == "**":
                        word = word[:-2]
                    if word[-1] == "*":
                        word = word[:-1]
                    return word

                if trim(nlvt) != trim(nrvt):
                    raise Exception(
                        f"Semantic Error; Can't assign address of '{nrvn}' of type '{nrvt}' to '{nlvn}' of Incorrect type '{nlvt}'.")

            # else: anders perfect in orde

        # Assignments of incompatible types "inta=1;floatb=a;" OF "inta;floatb;a=b;"
        # bv "int a; float b; a=b;"
        if node.left.type == "variable" and node.right.type == "variable":
            nodeLn = str(node.left.name)
            nodeRn = str(node.right.name)
            nodeLt = self.symbol_table.get_symbol(nodeLn)['type']
            nodeRt = self.symbol_table.get_symbol(nodeRn)['type']
            if nodeLt != nodeRt:
                raise Exception(
                    f"Variable '{nodeRn}' of type '{nodeRt}' gets assigned to variable '{nodeLn}' of incompatible type '{nodeLt}'. ")

        # bv "int a = 1; float b = a;"
        if node.left.type == "instantiation" and node.right.type == "variable":
            nodeLn = str(node.left.name)
            nodeRn = str(node.right.name)
            nodeLt = str(node.left.varType)
            nodeRt = self.symbol_table.get_symbol(nodeRn)['type']

            if node.left.const:
                nodeLt = "const" + nodeLt

            if nodeLt != nodeRt:
                raise Exception(
                    f"Syntax Error; During definition, Variable '{nodeRn}' of type '{nodeRt}' gets assigned to variable '{nodeLn}' of incompatible type '{nodeLt}'. ")
        return node

    def visitDeclaration(self, ctx: CParser.DeclarationContext, line_nr:int = -1):
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
                if type1[-1] == "*":
                    pass
                else:
                    raise Exception(
                        f"Semantic Error; Assignment to the const variable '{str(node.name)}' that has the type '{type1}'.")

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
        self.symbol_table.add_symbol(str(node.name), "const" + str(node.varType))

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
            # bv int a = 1;
            return self.visitFactor(ctx.factor(0))
        node = TermNode()
        node.operation = ctx.termops().getText()
        node.left = self.visitFactor(ctx.factor(0))
        if ctx.term():
            node.right = self.visitTerm(ctx.term())
        else:
            # bv ... = . + .;
            node.right = self.visitFactor(ctx.factor(1))
        node.children = [node.left, node.right]
        # bv int a = 1+2; =>  node.left.value = 1      node.right.value = 2
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
            if "\\" in node.value:
                node.value = eval('"' + node.value + '"')
            node.literalType = 'char'

        return node
