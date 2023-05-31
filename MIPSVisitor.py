from Nodes import *
from AST import AST
from SymbolTable import SymbolTable
from MIPSOperations import *

class MIPSVisitor:
    def __init__(self):
        self.file = ""
        self.data = [".data"]
        self.text = [".text"]
        self.treg = 0
        self.sreg = 0
        self.sp = 0
        self.fp = 0
        self.symbolTable: SymbolTable = SymbolTable([0])
        # block labels
        self.blocks = []
        self.cur_new_label = "L"

    def includeStdio(self):
        pass


    def visitRun(self, node: RunNode):
        if node.include:
            self.includeStdio()
        for child in node.children:
            child.generateMips(self)

        # write result to file
        file = open(self.file, "w")
        for instruction in self.text:
            file.write(instruction + '\n')
        file.close()

    def increase_label(self):
        integer = int(self.cur_new_label[1:])
        self.cur_new_label = "L" + str(integer + 1)

    def visitIf(self, node: IfNode):
        self.increase_label()
        else_label = self.cur_new_label

        # First parse Node Condition
        nc = node.condition
        #TODO De TermNode in de condition nog omzetten naar MIPS
        parsed_nc: list[str] = handle_condition_if(nc, else_label) # Parsed Node Condition

        # nc = Als de conditie niet waar is, springen we over het 'if' block:

        for i in parsed_nc:
            self.text.append(i)

        # Now parse If block
        self.visitBlock(node.block)

        # Als er een 'else' is, hierover heen springen
        else_node = False
        if node.elseNode:
            else_node = True
            self.increase_label()
            next_label: str = self.cur_new_label
            self.text.append("j " + next_label)

        # Now parse Else block
        self.text.append(else_label + ": ")
        if else_node:
            self.visitBlock(node.elseNode.block)


    def visitWhile(self, node: WhileNode):
        condition = node.condition
        block = node.block

        # Start of While block
        self.increase_label()
        while_label: str = self.cur_new_label
        self.instructions.append(while_label + ": ")

        # Parse Condition
        self.increase_label()
        done_label: str = self.cur_new_label
        parsed_condition = handle_condition_if(condition, done_label)

        for i in parsed_condition:
            self.instructions.append(i)

        # Parse While block
        self.visitBlock(block)

        # At end of while block, jump back to begin of While
        self.instructions.append("j " + while_label)

    def visitInstantiation(self, node: InstantiationNode, global_var):
        variable = None
        if global_var:
            variable = self.declareGlobal(node.name, node.varType)
        else:
            variable = self.declareLocal(node.varType)

        self.symbolTable.add_symbol(variable)

        return variable

    def declareGlobal(self, name, type):
        if type == "int" or type == "bool":
            type = "word"
        elif type == "char":
            type = "byte"
        elif type == "float":
            type = "float"
        else:
            print(f"error {type} ")
        self.data.append(f"{name}: .{type} 0")
        return Global(name, type)

    def declareLocal(self, type):
        size = 0
        if type == "int":
            self.sp -= 4
            size = 4
            type = "word"
        elif type == "char":
            self.sp -= 1
            size = 1
            type = "byte"
        elif type == "float":
            self.sp -= 4
            size = 4
            type = "float"
        elif type == "bool":
            self.sp -= 4
            size = 4
            type = "word"
        self.text.append(f"addi $sp, $sp, -{size}")
        return Local(self.sp, type)

    def visitVariable(self, node: VariableNode):
        #symbol = self.symbolTable[node.name]
        symbol = self.symbolTable.get_symbol(node.name)
        return symbol

    def visitLiteral(self, node: LiteralNode):
        return convertNode(node)

    def visitAssignment(self, node: AssignmentNode):
        variable = node.left.generateCode(self)

        # implicit conversion
        if node.right.type == "literal" and "float" in variable.varType:
            if node.right.literalType == "int":
                node.right.literalType = "float"

        result = node.right.generateCode(self)

        if result.address:
            self.instructions.append(store(result, variable))
            return
        tempResult = result
        result = self.getValue(result)

        # als result al één of meerdere keren gedereferenced werd, dan zal het niet opnieuw gebeuren
        # in getValue() wat wel moet
        if tempResult == result and result.varType[-1] == "*":
            temp = load(self.tempVar(), result)
            result = temp[0]
            self.instructions.append(temp[1])
        self.instructions.append(store(result, variable))

    def visitLogic(self, node: LogicNode):
        leftVal = self.getValue(node.left.generateCode(self))
        rightVal = self.getValue(node.right.generateCode(self))
        temp = self.richerConversion(leftVal, rightVal)
        leftVal = temp[0]
        rightVal = temp[1]
        floatType = temp[2]
        if floatType:
            if node.operation == "&&":
                temp = fcmpLogic("and", self.tempVar(), self.tempVar(), self.tempVar(), leftVal, rightVal)
            elif node.operation == "||":
                temp = fcmpLogic("or", self.tempVar(), self.tempVar(), self.tempVar(), leftVal, rightVal)
        else:
            if node.operation == "&&":
                temp = logic("and", self.tempVar(), leftVal, rightVal)
            elif node.operation == "||":
                temp = logic("or", self.tempVar(), leftVal, rightVal)
        result = temp[0]
        self.instructions.append(temp[1])
        return result

    def visitCompare(self, node: CompareNode):
        leftVal = self.getValue(node.left.generateCode(self))
        rightVal = self.getValue(node.right.generateCode(self))
        keyword = ""
        temp = self.richerConversion(leftVal, rightVal)
        leftVal = temp[0]
        rightVal = temp[1]
        floatType = temp[2]
        if floatType:
            if node.operation == "<":
                keyword = "olt"
            elif node.operation == "<=":
                keyword = "ole"
            elif node.operation == "==":
                keyword = "oeq"
            elif node.operation == "!=":
                keyword = "one"
            elif node.operation == ">=":
                keyword = "oge"
            elif node.operation == ">":
                keyword = "ogt"
            temp = fcmp(keyword, self.tempVar(), leftVal, rightVal)
            result = temp[0]
            self.instructions.append(temp[1])
        else:
            if node.operation == "<":
                keyword = "slt"
            elif node.operation == "<=":
                keyword = "sle"
            elif node.operation == "==":
                keyword = "eq"
            elif node.operation == "!=":
                keyword = "ne"
            elif node.operation == ">=":
                keyword = "sge"
            elif node.operation == ">":
                keyword = "sgt"
            temp = icmp(keyword, self.tempVar(), leftVal, rightVal)
            result = temp[0]
            self.instructions.append(temp[1])
        return result

    def visitTerm(self, node: TermNode):
        leftVal = self.getValue(node.left.generateCode(self))
        rightVal = self.getValue(node.right.generateCode(self))
        temp = self.richerConversion(leftVal, rightVal)
        leftVal = temp[0]
        rightVal = temp[1]
        floatType = temp[2]
        if floatType:
            if node.operation == "+":
                temp = fadd(self.tempVar(), leftVal, rightVal)
            elif node.operation == "-":
                temp = fsub(self.tempVar(), leftVal, rightVal)
        else:
            if node.operation == "+":
                temp = add(self.tempVar(), leftVal, rightVal)
            elif node.operation == "-":
                temp = sub(self.tempVar(), leftVal, rightVal)
        result = temp[0]
        self.instructions.append(temp[1])
        return result

    def visitFactor(self, node: FactorNode):
        leftVal = self.getValue(node.left.generateCode(self))
        rightVal = self.getValue(node.right.generateCode(self))
        temp = self.richerConversion(leftVal, rightVal)
        leftVal = temp[0]
        rightVal = temp[1]
        floatType = temp[2]
        if floatType:
            if node.operation == "*":
                temp = fmul(self.tempVar(), leftVal, rightVal)
            elif node.operation == "/":
                temp = fdiv(self.tempVar(), leftVal, rightVal)
            elif node.operation == "%":
                toInt = fptosi(self.tempVar(), leftVal)
                leftVal = toInt[0]
                self.instructions.append(toInt[1])
                toInt = fptosi(self.tempVar(), rightVal)
                rightVal = toInt[0]
                self.instructions.append(toInt[1])
                temp = urem(self.tempVar(), leftVal, rightVal)
        else:
            if node.operation == "*":
                temp = mul(self.tempVar(), leftVal, rightVal)
            elif node.operation == "/":
                temp = div(self.tempVar(), leftVal, rightVal)
            elif node.operation == "%":
                temp = urem(self.tempVar(), leftVal, rightVal)
        result = temp[0]
        self.instructions.append(temp[1])
        return result

    def visitUnary(self, node: UnaryNode):
        val = node.variable.generateCode(self)
        if node.operation == "&":
            val.address = True
            return val
        elif node.operation == "*":
            temp = load(self.tempVar(), val)
            result = temp[0]
            self.instructions.append(temp[1])
            return result
        val = self.getValue(val)
        temp = None
        floatType = False
        if val.varType == "float":
            floatType = True
        if node.operation == "-":
            if floatType:
                temp = fneg(self.tempVar(), val)
            else:
                temp = neg(self.tempVar(), val)
        elif node.operation == "!":
            if floatType:
                toInt = fptosi(self.tempVar(), val)
                val = toInt[0]
                self.instructions.append(toInt[1])
            temp = xor(self.tempVar(), val, LlvmType("i32", 1))
        result = temp[0]
        self.instructions.append(temp[1])
        return result

    def visitTypeCast(self, node: TypeCastNode):
        value = self.getValue(node.variable.generateCode(self))
        cast = node.castTo
        newValue = None
        if cast == "float" and value.varType != "float":
            conversion = sitofp(self.tempVar(), value)
            value = conversion[0]
            self.instructions.append(conversion[1])
        elif cast != "float" and value.varType == "float":
            conversion = fptosi(self.tempVar(), value)
            value = conversion[0]
            self.instructions.append(conversion[1])
        if ((cast == "float" and value.varType == "float") or
                (cast == "int" and value.varType == "i32") or
                (cast == "char" and value.varType == "i8") or
                (cast == "bool" and value.varType == "i1")):
            newValue = value
        elif cast != value.varType:
            conversion = None
            if cast == "int":
                conversion = zext(self.tempVar(), value, "i32")
            elif cast == "char":
                if value.varType == "i32":
                    conversion = trunc(self.tempVar(), value, "i8")
                elif value.varType == "i1":
                    conversion = zext(self.tempVar(), value, "i8")
            elif cast == "bool":
                conversion = trunc(self.tempVar(), value, "i1")
            newValue = conversion[0]
            self.instructions.append(conversion[1])

        return newValue

    def visitSpecialUnary(self, node: SpecialUnaryNode):
        val = node.variable.generateCode(self)
        temp = None
        floatType = False
        if val.varType == "float":
            floatType = True
        if node.operation == "++":
            if floatType:
                temp = fadd(self.tempVar(), val, LlvmType("float", 1))
            else:
                temp = add(self.tempVar(), val, LlvmType("i32", 1))
        elif node.operation == "--":
            if floatType:
                temp = fsub(self.tempVar(), val, LlvmType("float", 1))
            else:
                temp = sub(self.tempVar(), val, LlvmType("i32", 1))
        result = temp[0]
        self.text.append(temp[1])
        return result

    def visitReturn(self, node:ReturnNode):
        type = node.returnValue # Is een Variable, Literal, Term, Function call, ...
        # Bv literal
        # De literal waarde steken in $2/$v0
        value = node.returnValue.value

        # Variabele
        # variabele waarde halen uit $fp met offset, en 'lw' in $2/$v0

        # Term
        # uitrekenen en steken in $2/$v0

        # Tenslotte " jr $ra "
        self.text.append("jr $ra")


    def visitFunction(self, node: FunctionNode):
        declaration = node.declaration
        label:str = declaration.name

        self.text.append("label"+ ": ")

        # De argumenten zullen steken in $4-7/$a0-3
        # Meteen steken in de $fp met offset met 'sw'

        # In dit blok wordt de return ook verwerkt
        self.visitBlock(node.block)