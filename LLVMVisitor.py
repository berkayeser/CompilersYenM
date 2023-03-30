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

    func_type = ir.FunctionType(int32, [])
    function = ir.Function(module, func_type, name="main")
    block = function.append_basic_block("entry")

    def visitRun(self, node: RunNode):
        for child in node.children:
            child.generateCode(self)
        print(str(self.module))

    def visitLine(self, node: LineNode):
        for child in node.children:
            child.generateCode(self)

    def visitStatement(self, node: StatementNode):
        self.block.instructions.insert(len(self.block.instructions), "; " + node.instruction)
        for child in node.children:
            child.generateCode(self)

    def visitComment(self, node: CommentNode):
        builder = ir.IRBuilder(self.block)
        self.block.instructions.insert(0, "; " + node.text[0:-1])

    def visitAssignment(self, node: AssignmentNode):
        for child in node.children:
            child.generateCode(self)

    def visitInstantiation(self, node: InstantiationNode):
        pass

    def visitVariable(self, node: VariableNode):
        pass

    def visitLiteral(self, node: LiteralNode):
        value = node.convertValType()
        if node.literalType == "int":
            return self.int32(value)
        elif node.literalType == "float":
            return self.float32(value)
        elif node.literalType == "char":
            return self.int32(value)
        elif node.literalType == "bool":
            return self.int32(value)

    def visitLogic(self, node: LogicNode):
        if node.left.type == "literal" and node.right.type == "literal":
            builder = ir.IRBuilder(self.block)
            result = builder.add(self.int32(node.left.convertValType()), self.int32(node.right.convertValType()))
            return result

    def visitCompare(self, node: CompareNode):
        if node.left.type == "literal" and node.right.type == "literal":
            builder = ir.IRBuilder(self.block)
            result = builder.add(self.int32(node.left.convertValType()), self.int32(node.right.convertValType()))
            return result

    def visitTerm(self, node: TermNode):
        leftVal = node.left.generateCode(self)
        rightVal = node.right.generateCode(self)
        builder = ir.IRBuilder(self.block)
        result = None
        if node.operation == "+":
            result = builder.fadd(leftVal, rightVal)
        elif node.operation == "-":
            result = builder.fsub(leftVal, rightVal)
        return result

    def visitFactor(self, node: FactorNode):
        leftVal = node.left.generateCode(self)
        rightVal = node.right.generateCode(self)
        builder = ir.IRBuilder(self.block)
        result = None
        if node.operation == "*":
            result = builder.fmul(leftVal, rightVal)
        elif node.operation == "/":
            result = builder.fdiv(leftVal, rightVal)
        elif node.operation == "%":
            result = builder.urem(leftVal, rightVal)
        return result

    def visitUnary(self, node: UnaryNode):
        val = node.variable.generateCode(self)
        builder = ir.IRBuilder(self.block)
        result = None
        if node.operation == "-":
            result = builder.fneg(val)
        elif node.operation == "!":
            result = builder.xor(val, self.int32(1))
        return result

    def visitSpecialUnary(self, node: SpecialUnaryNode):
        val = node.variable.generateCode(self)
        builder = ir.IRBuilder(self.block)
        result = None
        if node.operation == "++":
            result = builder.fadd(val, self.int32(1))
        elif node.operation == "--":
            result = builder.fsub(val, self.int32(1))
        return result
