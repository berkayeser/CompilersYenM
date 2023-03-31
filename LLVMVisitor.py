from Nodes import *
from llvmlite import ir, binding


class LLVMVisitor:
    float32 = ir.FloatType()
    int32 = ir.IntType(32)

    module = ir.Module(name="C_compiler")

    binding.initialize()
    binding.initialize_native_target()
    binding.initialize_native_asmprinter()

    target = binding.Target.from_default_triple()
    target_machine = target.create_target_machine()
    data_layout = target_machine.target_data

    func_type = ir.FunctionType(ir.IntType(1), [])
    function = ir.Function(module, func_type, name="main")
    block = function.append_basic_block("entry")

    def visitRun(self, node: RunNode):
        for child in node.children:
            child.generateCode(self)
        builder = ir.IRBuilder(self.block)
        builder.ret(ir.Constant(ir.IntType(1), 0))
        print(str(self.module))

    def visitLine(self, node: LineNode):
        if node.comment:
            node.comment.generateCode(self)
        if node.statement:
            node.statement.generateCode(self)

    def visitStatement(self, node: StatementNode):
        self.block.instructions.insert(len(self.block.instructions), "; " + node.instruction)
        for child in node.children:
            child.generateCode(self)

    def visitComment(self, node: CommentNode):
        self.block.instructions.insert(len(self.block.instructions), "; " + node.text[0:-1])

    def visitAssignment(self, node: AssignmentNode):
        builder = ir.IRBuilder(self.block)
        result = node.right.generateCode(self)
        if node.left:
            variable = node.left.generateCode(self)
            builder.store(result, variable)

    def visitInstantiation(self, node: InstantiationNode):
        variable = None
        builder = ir.IRBuilder(self.block)
        if node.varType == "float":
            variable = builder.alloca(ir.FloatType(), name="g")
        else:
            variable = builder.alloca(ir.IntType(32), name="g")
            builder.store(ir.Constant(ir.IntType(32), 0), variable)
        return variable

    def visitVariable(self, node: VariableNode):
        builder = ir.IRBuilder(self.block)
        variable = builder.alloca(ir.FloatType(), name="my_variable")
        function = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), "my_function")

        # Get the variable by name using get_global
        retrieved_variable = self.module.get_global("my_variable")
        assert retrieved_variable is variable
        return self.module.get_global(name="g")

    def visitLiteral(self, node: LiteralNode):
        value = node.convertValType()
        if node.literalType == "float":
            return ir.Constant(ir.FloatType(), value)
        return ir.Constant(ir.IntType(32), value)

    def visitLogic(self, node: LogicNode):
        leftVal = node.left.generateCode(self)
        rightVal = node.right.generateCode(self)
        builder = ir.IRBuilder(self.block)
        result = None
        floatType = False
        if leftVal.type.intrinsic_name == "f32" or rightVal.type.intrinsic_name == "f32":
            floatType = True
            leftVal = builder.sitofp(leftVal, ir.FloatType())
            rightVal = builder.sitofp(rightVal, ir.FloatType())
        if floatType:
            cmp1 = builder.fcmp_ordered("one", leftVal, ir.Constant(ir.FloatType(), 0.0))
            cmp2 = builder.fcmp_ordered("one", rightVal, ir.Constant(ir.FloatType(), 0.0))
            if node.operation == "&&":
                result = builder.zext(builder.and_(cmp1, cmp2), ir.IntType(32))
            elif node.operation == "||":
                result = builder.zext(builder.or_(cmp1, cmp2), ir.IntType(32))
        else:
            if node.operation == "&&":
                result = builder.zext(builder.and_(leftVal, rightVal), ir.IntType(32))
            elif node.operation == "||":
                result = builder.zext(builder.or_(leftVal, rightVal), ir.IntType(32))
        return result

    def visitCompare(self, node: CompareNode):
        leftVal = node.left.generateCode(self)
        rightVal = node.right.generateCode(self)
        builder = ir.IRBuilder(self.block)
        result = None
        floatType = False
        keyword = ""
        if leftVal.type.intrinsic_name == "f32" or rightVal.type.intrinsic_name == "f32":
            floatType = True
            leftVal = builder.sitofp(leftVal, ir.FloatType())
            rightVal = builder.sitofp(rightVal, ir.FloatType())
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
            result = builder.zext(builder.fcmp_ordered(keyword, leftVal, rightVal), ir.IntType(32))
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
            result = builder.zext(builder.icmp_signed(keyword, leftVal, rightVal), ir.IntType(32))
        return result

    def visitTerm(self, node: TermNode):
        leftVal = node.left.generateCode(self)
        rightVal = node.right.generateCode(self)
        builder = ir.IRBuilder(self.block)
        result = None
        floatType = False
        if leftVal.type.intrinsic_name == "f32" or rightVal.type.intrinsic_name == "f32":
            floatType = True
            leftVal = builder.sitofp(leftVal, ir.FloatType())
            rightVal = builder.sitofp(rightVal, ir.FloatType())
        if node.operation == "+":
            if floatType:
                result = builder.fadd(leftVal, rightVal)
            else:
                result = builder.add(leftVal, rightVal)
        elif node.operation == "-":
            if floatType:
                result = builder.fsub(leftVal, rightVal)
            else:
                result = builder.sub(leftVal, rightVal)
        return result

    def visitFactor(self, node: FactorNode):
        leftVal = node.left.generateCode(self)
        rightVal = node.right.generateCode(self)
        builder = ir.IRBuilder(self.block)
        result = None
        floatType = False
        if leftVal.type.intrinsic_name == "f32" or rightVal.type.intrinsic_name == "f32":
            floatType = True
            leftVal = builder.sitofp(leftVal, ir.FloatType())
            rightVal = builder.sitofp(rightVal, ir.FloatType())
        if node.operation == "*":
            if floatType:
                result = builder.fmul(leftVal, rightVal)
            else:
                result = builder.mul(leftVal, rightVal)
        elif node.operation == "/":
            if floatType:
                result = builder.fdiv(leftVal, rightVal)
            else:
                result = builder.sdiv(leftVal, rightVal)
        elif node.operation == "%":
            result = builder.urem(leftVal, rightVal)
        return result

    def visitUnary(self, node: UnaryNode):
        val = node.variable.generateCode(self)
        builder = ir.IRBuilder(self.block)
        result = None
        floatType = False
        if val.type.intrinsic_name == "f32":
            floatType = True
        if node.operation == "-":
            if floatType:
                result = builder.fneg(val)
            else:
                result = builder.neg(val)
        elif node.operation == "!":
            if floatType:
                val = builder.fptosi(val, ir.IntType(32))
            result = builder.xor(val, ir.Constant(ir.IntType(32),1))
        return result

    def visitSpecialUnary(self, node: SpecialUnaryNode):
        val = node.variable.generateCode(self)
        builder = ir.IRBuilder(self.block)
        result = None
        floatType = False
        if val.type.intrinsic_name == "f32":
            floatType = True
        if node.operation == "++":
            if floatType:
                result = builder.fadd(val, ir.Constant(ir.FloatType(), 1))
            else:
                result = builder.add(val, ir.Constant(ir.IntType(32), 1))
        elif node.operation == "--":
            if floatType:
                result = builder.fsub(val, ir.Constant(ir.FloatType(), 1))
            else:
                result = builder.sub(val, ir.Constant(ir.IntType(32), 1))
        return result
