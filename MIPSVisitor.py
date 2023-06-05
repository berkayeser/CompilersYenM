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
        self.sp = 2147479548
        self.fp = 0

        # Symbol Tables
        self.symbol_table: SymbolTable = SymbolTable([0])
        self.cur_symbol_table: SymbolTable = self.symbol_table

        # block labels
        self.blocks = []

        self.if_label: int = -1
        self.while_label: int = -1
        self.printf_label: int = -1
        self.scanf_label: int = -1


    def exit(self):
        self.text.append("\n# End MIPS Program")
        self.text.append("li $v0, 10")
        self.text.append("syscall")

    def visitRun(self, node: RunNode):
        if node.include:
            self.includeStdio()
        for child in node.children:
            child.generateMips(self)

        # Exit syscall
        self.exit()

        # write result to file
        file = open(self.file, "w")
        for data in self.data:
            file.write(data + '\n')
        for text in self.text:
            file.write(text + '\n')
        file.close()

    def increase_if_label(self) -> str:
        self.if_label = self.if_label + 1
        new_index: int = self.if_label
        return "IF_" + str(new_index)

    def increase_while_label(self) -> str:
        self.while_label = self.while_label + 1
        new_index: int = self.while_label
        return "WHILE_" + str(new_index)

    def increase_printf_label(self) -> str:
        self.printf_label = self.printf_label + 1
        new_index: int = self.printf_label
        return "printf_" + str(new_index)

    def increase_scanf_label(self) -> str:
        self.scanf_label = self.scanf_label + 1
        new_index: int = self.scanf_label
        return "scanf_" + str(new_index)

    def visitIf(self, node: IfNode):
        else_label = self.increase_if_label()

        # First parse Node Condition
        parsed_condition: list[str] = handle_condition(node.condition, else_label) # Parsed Node Condition

        # nc = Als de conditie niet waar is, springen we over het 'if' block:

        for i in parsed_condition:
            self.text.append(i)

        # Now parse If block
        node.block.generateMips(self)

        # Als er een 'else' is, hierover heen springen
        else_node = False
        if node.elseNode:
            else_node = True
            next_label: str = "next_" + str(self.if_label)
            self.text.append("j " + next_label)

        # Now parse Else block
        self.text.append(else_label + ": ")
        if else_node:
            node.elseNode.block.generateMips(self)
            self.text.append(next_label + ":")


    def visitWhile(self, node: WhileNode):
        # Start of While block
        while_label: str = self.increase_while_label()
        self.text.append(while_label + ": ")

        # Parse Condition
        done_label: str = "WHILE_DONE_" + str(self.while_label)
        parsed_condition = handle_condition(node.children[0], done_label)

        for i in parsed_condition:
            self.text.append(i)

        # Parse While block
        node.block.generateMips(self)

        # At end of while block, jump back to begin of While
        self.text.append("j " + while_label)
        self.text.append(done_label + ":")


    def visitInstantiation(self, node: InstantiationNode, global_var):
        if global_var:
            variable = self.declareGlobal(node.name, node.varType)
        else:
            variable = self.declareLocal(node.varType)

        if type(node.name) != str:
            nn = node.name.getText()
        else:
            nn = node.name
        self.cur_symbol_table.add_symbol(nn, variable.type, False, variable)

        return variable

    def visitArrayInstantiation(self, node: ArrayInstantiationNode, global_var):
        if global_var:
            variable = self.declareGlobalArray(node.name, node.type, node.size)
        else:
            variable = self.declareLocalArray(node.type, node.size)

        if type(node.name) != str:
            nn = node.name.getText()
        else:
            nn = node.name
        self.cur_symbol_table.add_symbol(nn, variable.type, False, variable)

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
            print(f"error151 {type} ")
        self.data.append(f"{name}: .{type} 0")
        return Global(name, type)

    def declareGlobalArray(self, name, type, size):
        singleSize = 0
        if type == "int" or type == "bool":
            singleSize = 4
            type = "word"
        elif type == "char":
            singleSize = 1
            type = "byte"
        elif "float" in type:
            singleSize = 4
            type = "float"
        self.data.append(f"{name}: .space {size * singleSize}")
        return GlobalArray(name, type, singleSize, size)

    def declareLocal(self, type):
        size = 0
        if type == "int" or type == "bool":
            size = 4
            type = "word"
        elif type == "char":
            size = 1
            type = "byte"
        elif "float" in type:
            size = 4
            type = "float"
        elif "*" in type:
            size = 4
            type = "word"
        self.sp -= size
        self.text.append(f"addi $sp, $sp, -{size}")
        return Local(self.sp, type)

    def declareLocalArray(self, type, size):
        singleSize = 0
        if type == "int" or type == "bool":
            singleSize = 4
            type = "word"
        elif type == "char":
            singleSize = 1
            type = "byte"
        elif "float" in type:
            singleSize = 4
            type = "float"
        self.sp -= size * singleSize
        self.text.append(f"addi $sp, $sp, -{size * singleSize}")
        return LocalArray(self.sp, type, singleSize, size)

    def visitVariable(self, node: VariableNode) -> Register:
        return self.cur_symbol_table.get_symbol(node.name)['reg']

    def getValue(self, variable):
        if isinstance(variable, Register):
            return variable

        if variable.type == "float":
            register_nr = self.freg
            self.freg += 1
        elif variable.type == "word" or variable.type == "byte":
            register_nr = self.treg
            self.treg += 1
        else:
            print("error224")

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

        result = self.getValue(node.right.generateMips(self))

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
            self.text.append(variable.storeLocal(result, self.sp))
        elif isinstance(variable, Global):
            self.text.append(variable.storeGlobal(result))
        elif isinstance(variable, Register):
            if variable.pointerAddress:
                if variable.type == "float":
                    return f"s.s {result}, ({variable.pointerAddress})"
                else:
                    return f"sw {result}, ({variable.pointerAddress})"
            elif variable.arrayAddress:
                if variable.type == "float":
                    return f"s.s {result}, ({variable.arrayAddress})"
                else:
                    return f"sw {result}, ({variable.arrayAddress})"


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
            index = Register()
            index.assign(self.treg, "t")
            if isinstance(register, Local):
                temp = register.loadLocal(register.register, self.sp)
                index.save(register.offset - self.sp)
            elif isinstance(register, Global):
                temp = register.loadGlobal(register.register)
                self.text.append(register.loadAdress(index.register))
            elif isinstance(register, Register):
                self.text.append(index.save(0))
                self.text.append(add(index, index, register))
                self.text.append(register.load(self.treg))
                register.pointerAddress = index
                return register
            temp[1].pointerAddress = index
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
        variable = node.variable.generateMips(self)  # Variable mag niet dict zijn
        value = self.getValue(variable)
        instruction = None
        floatType = (value.type == "f")
        if node.operation == "++":
            if floatType:
                tempRegister = Register()
                tempRegister.assign(self.freg, "f")
                self.text.append(tempRegister.save(1, self.treg))
                instruction = add(value, value, tempRegister)
            else:
                instruction = addi(value, value, 1)
        elif node.operation == "--":
            if floatType:
                tempRegister = Register()
                tempRegister.assign(self.freg, "f")
                self.text.append(tempRegister.save(1, self.treg))
                instruction = sub(value, value, tempRegister)
            else:
                instruction = subi(value, value, 1)
        self.text.append(instruction)
        # store new value in variable
        if isinstance(variable, Global):
            variable.storeGlobal(value)
        elif isinstance(variable, Local):
            variable.storeLocal(value, self.sp)
        # pointer and array
        else:
            if variable.pointerAddress:
                if variable.type == "float":
                    return f"s.s {value}, ({variable.pointerAddress})"
                else:
                    return f"sw {value}, ({variable.pointerAddress})"
            elif variable.arrayAddress:
                if variable.type == "float":
                    return f"s.s {value}, ({variable.arrayAddress})"
                else:
                    return f"sw {value}, ({variable.arrayAddress})"
        return value

    def visitArray(self, node: ArrayNode):
        array = self.cur_symbol_table.get_symbol(node.name)
        # Has to be int (t register)
        index = self.getValue(node.index.generateMips(self))
        result = None
        # index * self.size
        temRegister = Register()
        temRegister.assign(self.treg, "t")
        self.text.append(temRegister.save(array.size))
        self.text.append(multiply(index, index, temRegister))
        if isinstance(array, GlobalArray):
            if array.type == "float":
                result = array.loadGlobal(self.freg, index)
                self.freg += 1
            else:
                result = array.loadGlobal(index.register, index)
            self.text.append(array.loadAddress(temRegister.register))
            self.text.append(add(index, index, temRegister))

        # (self.offset - sp) + index
        elif isinstance(array, LocalArray):
            self.text.append(temRegister.save(array.offset))
            self.text.append(subi(temRegister, temRegister, self.sp))
            self.text.append(add(index, index, temRegister))
            if array.type == "float":
                result = array.loadLocal(self.freg, index)
                self.freg += 1
            else:
                result = array.loadLocal(index.register, index)

        result[1].arrayAddress = index
        self.text.append(result[0])
        return result[1]

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

    def visitBreak(self, node: BreakNode):
        pass

    def visitContinue(self, node: ContinueNode):
        pass

    def visitFunction(self, node: FunctionNode):
        declaration = node.declaration
        label: str = declaration.name
        main_flag: bool = False
        if label == "main":
            main_flag = True
            self.text.append(".globl main")

        self.text.append(label + ": ")

        # Functie argumenten parsen
        # De argumenten zullen steken in $4-7/$a0-3
        # We steken deze in de $fp met offset met 'sw'
        amt = len(declaration.arguments)
        if amt > 4:
            raise Exception("Too many arguments.")
        offset: int = (amt-1) * 4
        for i in range(0, amt):
            a: str = "$a" + str(i)
            self.text.append(f"sw {a}, {str(offset)}($fp)")
            offset -= 4


        # Het blok van de functie
        # In dit blok wordt de return ook verwerkt
        nodeblock: BlockNode = node.block
        nodeblock.generateMips(self)

        # zwz op het einde van de function returnen ( zelfs als er geen return in de functie staat )
        # behalve in int main()
        if not main_flag:
            self.text.append("jr $ra")

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
        new_name = self.cur_symbol_table.name.copy()
        new_id = 0 + len(self.cur_symbol_table.subScopes)
        new_name.append(new_id)
        new_st = SymbolTable(new_name)
        new_st.parentScope = self.cur_symbol_table
        self.cur_symbol_table.subScopes.append(new_st)
        self.cur_symbol_table = new_st

        for statement in node.children:
            statement.generateMips(self)

        self.cur_symbol_table = self.cur_symbol_table.parentScope

    def visitExpressionStatement(self, node: ExpressionStatementNode):
        for statement in node.children:
            statement.generateMips(self)

    def visitPrintf(self, node: PrintfNode):
        #self.text.append("addi $sp, $sp, -4")
        #self.text.append("sw $a0, 0($sp)")

        # Parse string with arguments
        s = parse_string(node.string, node.arguments)
        label: str = self.increase_printf_label()

        # Put string into data
        self.data.append(f"{label}: .asciiz {s}")
        # Put string into $a0
        self.text.append(f"la $a0, {label}")

        # Call Printf Function
        self.text.append("jal printf")

        #self.text.append("lw $a0, 0($sp)")
        #self.text.append("addi $sp, $sp, 4")

    def visitScanf(self, node: ScanfNode):
        int = "%d"
        float = "%f"
        char = "%c"
        string = "%s"
        value = None

        # Parse string
        parsed = compile_scanf_string(node.string)
        for i in range(0, len(parsed)):
            variable_name: str = node.arguments[i].value.variable.name

            # bv. arg: string/int/float/char = &x

            register = self.cur_symbol_table.get_symbol(variable_name)['reg']
            r: str = str(register.register)
            if register.type == "s":
                dest = "$s" + r
            elif register.type == "t":
                dest = "t" + r
            else:
                dest = "t" + r

            if parsed[i] in [char, string]:
                label = self.increase_scanf_label()
                self.data.append(f"{label}: .space 61")
                self.text.append("la $a0, " + label)
                self.text.append("li $a1, 61")

                # Call Scanf Function
                self.text.append("jal scanf_string")
                # Input in {label}

                self.text.append(f"la ${dest} , {label}\n")
            elif parsed[i] == int:
                self.text.append("jal scanf_int")
                # Input in $v0
                dest = None

                    #print("error660" + register.type)

                self.text.append(f"la ${dest} , ($v0)\n")


            # TODO 2) Value plaatsen in juiste register
            #self.cur_symbol_table.add_symbol_value(variable_name, value)


    def visitFunction_call(self, node: CallNode):
        # Arguments in registers a0-3 plaatsen
        for i in node.arguments:
            if i.type == "literal":
                pass
            elif i.type == "variable":
                pass

        # Functie oproepen
        self.text.append("jal " + node.name)

    def includeStdio(self):
        # Printf functie implementeren
        # Value to be printed needs to be in $a0
        self.text.append("printf:")
        self.text.append("li $v0, 4") # Print String
        self.text.append("syscall")
        self.text.append("jr $ra")

        self.text.append("")

        # Scanf functie implementeren
        self.text.append("scanf_string:")
        self.text.append("li $v0, 8")
        self.text.append("syscall")
        self.text.append("jr $ra")
        # User Input will be in {label}

        self.text.append("")

        self.text.append("scanf_int:")
        self.text.append("li $v0, 5")
        self.text.append("syscall")
        self.text.append("jr $ra")
        # User Input will be in $v0



    def visitComment(self, node: CommentNode):
        self.text.append("# " + node.text)


