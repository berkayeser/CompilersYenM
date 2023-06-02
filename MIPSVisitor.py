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
        self.freg = 0
        self.sreg = 0
        self.sp = 0
        self.fp = 0
        self.symbolTable: SymbolTable = SymbolTable([0])
        # block labels
        self.blocks = []
        self.cur_new_label = "L"



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
        register = self.symbolTable.get_symbol(node.name)
        if register.type == "f":
            register_nr = self.freg
            self.freg += 1
        else:
            register_nr = self.treg
            self.treg += 1

        if isinstance(register, Global):
            temp = register.loadGlobal(register_nr)
            self.text.append(temp[0])
            register = temp[1]
        elif isinstance(register, Local):
            temp = register.loadLocal(register_nr, self.sp)
            self.text.append(temp[0])
            register = temp[1]

        return register

    def visitLiteral(self, node: LiteralNode):
        value = node.convertValType()
        nlt = str(node.literalType)
        register = Register()
        if nlt == "int":
            register.assign(self.treg, "t")
            self.text.append(register.load(value))
        elif nlt == "float":
            register.assign(self.freg, "f")
            self.text.append(register.load(float_to_64bit_hex(value)))
        elif nlt == "char":
            register.assign(self.treg, "t")
            self.text.append(register.load(value))
        elif nlt == "bool":
            register.assign(self.treg, "t")
            if value:
                self.text.append(register.load(1))
            else:
                self.text.append(register.load(0))
        return register

    # def visitAssignment(self, node: AssignmentNode):
    #     variable = node.left.generateCode(self)
    #
    #     # implicit conversion
    #     if node.right.type == "literal" and "float" in variable.varType:
    #         if node.right.literalType == "int":
    #             node.right.literalType = "float"
    #
    #     result = node.right.generateCode(self)
    #
    #     if result.address:
    #         self.instructions.append(store(result, variable))
    #         return
    #     tempResult = result
    #     result = self.getValue(result)
    #
    #     # als result al één of meerdere keren gedereferenced werd, dan zal het niet opnieuw gebeuren
    #     # in getValue() wat wel moet
    #     if tempResult == result and result.varType[-1] == "*":
    #         temp = load(self.tempVar(), result)
    #         result = temp[0]
    #         self.instructions.append(temp[1])
    #     self.instructions.append(store(result, variable))

    def visitLogic(self, node: LogicNode):
        lRegister = node.left.generateMips(self)
        rRegister = node.right.generateMips(self)
        temp = self.poorerConversion(lRegister, rRegister)
        lRegister = temp[0]
        rRegister = temp[1]
        instruction = ""
        if node.operation == "&&":
            instruction = logical_and(lRegister, lRegister, rRegister)
        elif node.operation == "||":
            instruction = logical_or(lRegister, lRegister, rRegister)
        self.treg -= 1
        self.text.append(instruction)
        return lRegister


    def visitCompare(self, node: CompareNode):
        lRegister = node.left.generateMips(self)
        rRegister = node.right.generateMips(self)
        temp = self.richerConversion(lRegister, rRegister)
        lRegister = temp[0]
        rRegister = temp[1]
        instruction = ""
        tempRegister = Register()
        if lRegister.type == "f":
            tempRegister.assign(self.treg, "t")
            self.text.append(tempRegister.load(1))
        instruction = compare(node.operation, lRegister, lRegister, rRegister, tempRegister)
        self.text.append(instruction)
        if rRegister.type == "f":
            self.freg -= 1
        elif rRegister.type == "s":
            self.sreg -= 1
        else:
            self.treg -= 1
        return lRegister

    def visitTerm(self, node: TermNode):
        lRegister = node.left.generateMips(self)
        rRegister = node.right.generateMips(self)
        temp = self.richerConversion(lRegister, rRegister)
        lRegister = temp[0]
        rRegister = temp[1]
        instruction = ""
        if rRegister.type == "f":
            self.freg -= 1
        elif rRegister.type == "s":
            self.sreg -= 1
        else:
            self.treg -= 1
        if node.operation == "+":
            instruction = add(lRegister, lRegister, rRegister)
        elif node.operation == "-":
            instruction = sub(lRegister, lRegister, rRegister)
        result = temp[0]
        self.text.append(instruction)
        return result

    def visitFactor(self, node: FactorNode):
        lRegister = node.left.generateMips(self)
        rRegister = node.right.generateMips(self)
        temp = self.richerConversion(lRegister, rRegister)
        lRegister = temp[0]
        rRegister = temp[1]
        if rRegister.type == "f":
            self.freg -= 1
        elif rRegister.type == "s":
            self.sreg -= 1
        else:
            self.treg -= 1
        instruction = ""
        if node.operation == "*":
            instruction = multiply(lRegister, lRegister, rRegister)
        elif node.operation == "/":
            instruction = divide(lRegister, lRegister, rRegister)
        elif node.operation == "%":
            instruction = modulo(lRegister, lRegister, rRegister)
        self.text.append(instruction)
        return lRegister

    def visitUnary(self, node: UnaryNode):
        register = node.variable.generateMips(self)
        # if node.operation == "&":
        #     register.address = True
        #     return register
        # if node.operation == "*":
        #     f"lw newRegister "
        #     temp = load(self.tempVar(), val)
        #     result = temp[0]
        #     self.instructions.append(temp[1])
        #     return result
        # register = self.getValue(register)
        instruction = ""
        floatType = register.type == "f"
        if node.operation == "-":
            self.text.append(neg(register, register))
        elif node.operation == "!":
            if floatType:
                register.assign(self.treg, "t")
                self.treg += 1
                self.freg -= 1
                self.text.append(convert_float_to_int(register, register))
            self.text.append(logical_not(register, register))
        elif node.operation == "+":
            return register
        return register

    def visitTypeCast(self, node: TypeCastNode):
        register = node.variable.generateMips(self)
        cast = node.castTo
        newRegister = Register()
        if cast == "float" and register.type != "f":
            newRegister.assign(self.freg, "f")
            self.freg += 1
            if register.type == "t":
                self.treg -= 1
            elif register.type == "s":
                self.sreg -= 1
            instruction = convert_int_to_float(newRegister, register)
        elif cast != "float" and register.type == "f":
            newRegister.assign(self.treg, "t")
            self.freg -= 1
            self.treg += 1
            instruction = convert_float_to_int(newRegister, register)
        else:
            newRegister = register
            instruction = ""

        self.text.append(instruction)
        return newRegister

    def visitSpecialUnary(self, node: SpecialUnaryNode):
        register = node.variable.generateMips(self)
        instruction = None
        floatType = (register.type == "f")
        if node.operation == "++":
            if floatType:
                tempRegister = Register()
                tempRegister.assign(self.freg, "f")
                self.text.append(tempRegister.load(1, self.treg))
                instruction = add(register, register, tempRegister)
            else:
                instruction = addi(register, register, 1)
        elif node.operation == "--":
            if floatType:
                tempRegister = Register()
                tempRegister.assign(self.freg, "f")
                self.text.append(tempRegister.load(1, self.treg))
                instruction = sub(register, register, tempRegister)
            else:
                instruction = subi(register, register, 1)
        self.text.append(instruction)
        return register

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

    def richerConversion(self, lRegister, rRegister):
        newRegister = Register()
        if (lRegister.type == "float" or rRegister.type == "float") and lRegister.type != rRegister.type:
            if rRegister.type != "f":
                newRegister.assign(self.freg, "f")
                self.freg += 1
                if rRegister.type == "t":
                    self.treg -= 1
                elif rRegister.type == "s":
                    self.sreg -= 1
                self.text.append(convert_int_to_float(newRegister, rRegister))
                rRegister = newRegister
            elif lRegister.type != "f":
                newRegister.assign(self.freg, "f")
                self.freg += 1
                if lRegister.type == "t":
                    self.treg -= 1
                elif lRegister.type == "s":
                    self.sreg -= 1
                self.text.append(convert_int_to_float(newRegister, lRegister))
                lRegister = newRegister
        return lRegister, rRegister

    def poorerConversion(self, lRegister, rRegister):
        newRegister = Register()
        if (lRegister.type == "float" or rRegister.type == "float") and lRegister.type != rRegister.type:
            if rRegister.type == "f":
                newRegister.assign(self.freg, "t")
                self.treg += 1
                self.freg -= 1
                self.text.append(convert_float_to_int(newRegister, rRegister))
                rRegister = newRegister
            elif lRegister.type == "f":
                newRegister.assign(self.freg, "t")
                self.treg += 1
                self.freg -= 1
                self.text.append(convert_float_to_int(newRegister, lRegister))
                lRegister = newRegister
        return lRegister, rRegister

    def visitBlock(self, node: BlockNode):
        for statement in node.children:
            statement.generateMips(self)

    def visitStatement(self, node: StatementNode):
        pass

    def includeStdio(self):
        pass

    def visitComment(self, node: CommentNode):
        pass

    #def visitLine(self, node:StatementNode):