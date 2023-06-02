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
        for data in self.data:
            file.write(data + '\n')
        for text in self.text:
            file.write(text + '\n')
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
        if global_var:
            variable = self.declareGlobal(node.name, node.varType)
        else:
            variable = self.declareLocal(node.varType)

        self.symbolTable.add_symbol(variable.name, variable.type)

        return variable

    def declareGlobal(self, name, type):
        if type == "int" or type == "bool":
            type = "word"
        elif type == "char":
            type = "byte"
        elif "float" in type:
            type = "float"
        elif "*" in type:
            type = "word"
        else:
            print(f"error {type} ")
        self.data.append(f"{name}: .{type} 0")
        return Global(name, type)

    def declareLocal(self, type):
        size = 0
        if type == "int" or type == "bool":
            self.sp -= 4
            size = 4
            type = "word"
        elif type == "char":
            self.sp -= 1
            size = 1
            type = "byte"
        elif "float" in type:
            self.sp -= 4
            size = 4
            type = "float"
        elif "*" in type:
            self.sp -= 4
            size = 4
            type = "word"
        self.text.append(f"addi $sp, $sp, -{size}")
        return Local(self.sp, type)

    def visitVariable(self, node: VariableNode):
        return self.symbolTable.get_symbol(node.name)

    def getValue(self, variable):
        if isinstance(variable, Register):
            return variable

        if variable.type == "f":
            register_nr = self.freg
            self.freg += 1
        else:
            register_nr = self.treg
            self.treg += 1

        if isinstance(variable, Global):
            temp = variable.loadGlobal(register_nr)
            self.text.append(temp[0])
            variable = temp[1]
        elif isinstance(variable, Local):
            temp = variable.loadLocal(register_nr, self.sp)
            self.text.append(temp[0])
            variable = temp[1]

        return variable

    def visitLiteral(self, node: LiteralNode):
        value = node.convertValType()
        nlt = str(node.literalType)
        register = Register()
        if nlt == "int":
            register.assign(self.treg, "t")
            self.text.append(register.save(value))
        elif nlt == "float":
            register.assign(self.freg, "f")
            self.text.append(register.save(float_to_64bit_hex(value)))
        elif nlt == "char":
            register.assign(self.treg, "t")
            self.text.append(register.save(value))
        elif nlt == "bool":
            register.assign(self.treg, "t")
            if value:
                self.text.append(register.save(1))
            else:
                self.text.append(register.save(0))
        return register

    def visitAssignment(self, node: AssignmentNode):
        variable = node.left.generateMips(self)

        # implicit conversion
        if node.right.type == "literal" and variable.type == "f":
            if node.right.literalType == "int":
                node.right.literalType = "float"

        result = self.getValue(node.right.generateCode(self))

        # conversion
        newRegister = Register()
        if variable.type != "float" and result.type == "f":
            newRegister.assign(self.freg, "t")
            self.treg += 1
            self.freg -= 1
            self.text.append(convert_float_to_int(newRegister, result))
            result = newRegister
        elif variable.type == "float" and result.type != "f":
            newRegister.assign(self.freg, "f")
            self.freg += 1
            if result.type == "t":
                self.treg -= 1
            elif result.type == "s":
                self.sreg -= 1
            self.text.append(convert_int_to_float(newRegister, result))
            result = newRegister

        if isinstance(variable, Local):
            self.text.append(storeLocal(variable, result, self.sp))
        elif isinstance(variable, Global):
            self.text.append(storeGlobal(variable, result))

    def storeGlobal(self, destination, register):
        if isinstance(register, Global):
            if destination.type == "float":
                return f"s.s $f{register.register}, {destination.name}"
            else:
                return f"sw $t{register.register}, {destination.name}"
        elif isinstance(register, Local):
            if destination.type == "float":
                return f"s.s {self.sp - destination.offset}($sp), {destination}"
            else:
                return f"sw {self.sp - destination.offset}($sp), {self.sp - destination.offset}($sp)"
        elif isinstance(register, Register):
            if destination.type == "float":
                return f"s.s {register}, {destination}"
            else:
                return f"sw {register}, {destination}"

    def visitLogic(self, node: LogicNode):
        lRegister = self.getValue(node.left.generateMips(self))
        rRegister = self.getValue(node.right.generateMips(self))
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
        lRegister = self.getValue(node.left.generateMips(self))
        rRegister = self.getValue(node.right.generateMips(self))
        temp = self.richerConversion(lRegister, rRegister)
        lRegister = temp[0]
        rRegister = temp[1]
        instruction = ""
        tempRegister = Register()
        if lRegister.type == "f":
            tempRegister.assign(self.treg, "t")
            self.text.append(tempRegister.save(1))
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
        lRegister = self.getValue(node.left.generateMips(self))
        rRegister = self.getValue(node.right.generateMips(self))
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
        lRegister = self.getValue(node.left.generateMips(self))
        rRegister = self.getValue(node.right.generateMips(self))
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
        if node.operation == "&":
            temp = None
            if isinstance(register, Local):
                temp = register.loadAddress(self.treg, self.sp)
            elif isinstance(register, Global):
                temp = register.loadAdress(self.treg)
            self.treg += 1
            self.text.append(temp[0])
            return temp[1]
        elif node.operation == "*":
            temp = None
            if isinstance(register, Local):
                if register.type == "float":
                    temp = register.loadLocal(self.freg, self.sp)
                    self.freg += 1
                else:
                    temp = register.loadLocal(self.treg, self.sp)
                    self.treg += 1
            elif isinstance(register, Global):
                if register.type == "float":
                    temp = register.loadGlobal(self.freg)
                    self.freg += 1
                else:
                    temp = register.loadGlobal(self.treg)
                    self.treg += 1
            elif isinstance(register, Register):
                temp = register.load(self.treg)
            self.text.append(temp[0])
            return temp[1]
        register = self.getValue(register)
        instruction = ""
        floatType = register.type == "f"
        register = self.getValue(register)
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
        register = self.getValue(node.variable.generateMips(self))
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
        register = self.getValue(node.variable.generateMips(self))
        instruction = None
        floatType = (register.type == "f")
        if node.operation == "++":
            if floatType:
                tempRegister = Register()
                tempRegister.assign(self.freg, "f")
                self.text.append(tempRegister.save(1, self.treg))
                instruction = add(register, register, tempRegister)
            else:
                instruction = addi(register, register, 1)
        elif node.operation == "--":
            if floatType:
                tempRegister = Register()
                tempRegister.assign(self.freg, "f")
                self.text.append(tempRegister.save(1, self.treg))
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

    def visitExpressionStatement(self, node: ExpressionStatementNode):
        for statement in node.children:
            statement.generateMips(self)


    def includeStdio(self):
        pass

    def visitComment(self, node: CommentNode):
        pass

