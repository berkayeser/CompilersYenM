import struct


class Node:
    children = []
    type = None

    def __init__(self):
        self.children = []

    def addNodes(self, nodes):
        self.children.append(nodes)

    def foldConstant(self):
        return None

    def getASTvalue(self):
        return self.type

    def generateCode(self, llvm):
        pass


class RunNode(Node):
    type = "run"
    include = False

    def generateCode(self, llvm):
        return llvm.visitRun(self)


class IncludeNode(Node):
    type = "include"
    lib = "stdio"


class FuncDeclareNode(Node):
    type = "function_declaration"
    name = ""
    returnType = ""
    arguments = []


class FunctionNode(Node):
    type = "function"
    declaration = None  # FuncDeclareNode
    block = []


class PrintfNode(Node):
    type = "printf"
    string = None
    arguments = []


class ScanfNode(Node):
    type = "scanf"
    string = None
    arguments = []


class FunctionArgNode(Node):
    type = "function_argument"
    const = None
    varType = None
    reference = None
    name = None


class CallNode(Node):
    type = "call"
    name = ""
    arguments = []


class ArgumentNode(Node):
    type = "argument"
    value = None


class BreakNode(Node):
    type = "break"

    def generateCode(self, llvm):
        return llvm.visitBreak(self)


class ContinueNode(Node):
    type = "continue"

    def generateCode(self, llvm):
        return llvm.visitContinue(self)


class ReturnNode(Node):
    type = "return"
    returnValue = None


class PrintNode(Node):
    type = "print"
    toPrint = ""

    def generateCode(self, llvm):
        return llvm.visitPrint(self)


class BlockNode(Node):
    type = "block"
    # all code inside
    block = None
    comment = ""

    def generateCode(self, llvm):
        for i in self.children:
            i.generateCode(llvm)


class StatementNode(Node):
    type = "line"
    statement = None
    comment = None

    def generateCode(self, llvm):
        return llvm.visitLine(self)


class IfNode(Node):
    type = "if"
    condition = None
    # all code inside
    block = None
    elseNode = None
    comment = None

    def generateCode(self, llvm):
        return llvm.visitIf(self)


class ElseNode(Node):
    type = "else"
    # all code inside
    block = None

    def generateCode(self, llvm):
        return llvm.visitElse(self)


class WhileNode(Node):
    type = "while"
    condition = None
    block = None
    comment = None

    def generateCode(self, llvm):
        return llvm.visitWhile(self)


class ExpressionStatementNode(Node):
    type = "statement"
    instruction = ""

    def getASTvalue(self):
        return self.instruction

    def generateCode(self, llvm):
        return llvm.visitExpressionStatement(self)


class CommentNode(Node):
    type = "comment"
    text = ""

    def getASTvalue(self):
        return self.text

    def generateCode(self, llvm):
        return llvm.visitComment(self)


class AssignmentNode(Node):
    type = "assignment"
    left = None
    right = None

    def generateCode(self, llvm):
        return llvm.visitAssignment(self)


class InstantiationNode(Node):
    type = "instantiation"
    const = False
    varType = ""  # type int, float, ...
    name = ""  # variable name x, y , ...

    def getASTvalue(self):
        return str(self.name)

    def generateCode(self, llvm):
        return llvm.visitInstantiation(self)


class VariableNode(Node):
    type = "variable"
    name = ""

    def getASTvalue(self):
        return str(self.name)

    def generateCode(self, llvm):
        return llvm.visitVariable(self)


class ArrayInstantiationNode(Node):
    type = "arrayInstantiation"
    name = ""
    size = None
    varType = ""


class ArrayNode(Node):
    type = "array"
    name = ""
    index = None


class LogicNode(Node):
    type = "logic"
    operation = ""
    left = None
    right = None

    def foldConstant(self):
        if self.left.type == "literal" and self.right.type == "literal":
            node = LiteralNode()
            leftVal = self.left.convertValType()
            rightVal = self.right.convertValType()
            node.literalType = "bool"

            if self.operation == "&&":
                node.value = str(leftVal and rightVal)
            elif self.operation == "||":
                node.value = str(leftVal or rightVal)
            return node
        return None

    def generateCode(self, llvm):
        return llvm.visitLogic(self)


class CompareNode(Node):
    type = "compare"
    operation = ""
    left = None
    right = None

    def foldConstant(self):
        if self.left.type == "literal" and self.right.type == "literal":
            node = LiteralNode()
            leftVal = self.left.convertValType()
            rightVal = self.right.convertValType()
            node.literalType = "bool"
            if self.operation == "<":
                node.value = str(leftVal < rightVal)
            elif self.operation == "<=":
                node.value = str(leftVal <= rightVal)
            elif self.operation == "==":
                node.value = str(leftVal == rightVal)
            elif self.operation == "!=":
                node.value = str(leftVal != rightVal)
            elif self.operation == ">=":
                node.value = str(leftVal >= rightVal)
            elif self.operation == ">":
                node.value = str(leftVal > rightVal)
            return node
        return None

    def generateCode(self, llvm):
        return llvm.visitCompare(self)


class TermNode(Node):
    type = "term"
    operation = ""
    left = None
    right = None

    def getASTvalue(self):
        return str(self.operation)

    def foldConstant(self):
        if self.left.type == "literal" and self.right.type == "literal":
            node = LiteralNode()
            leftVal = self.left.convertValType()
            rightVal = self.right.convertValType()
            Ltype = self.left.literalType
            Rtype = self.right.literalType
            if Ltype == "float" or Rtype == "float":
                node.literalType = "float"
            else:
                node.literalType = "int"
            if Ltype == "char":
                leftVal = ord(leftVal[1:-1])
            if Rtype == "char":
                temp = rightVal[1:-1]
                rightVal = ord(temp)

            if self.operation == "+":
                node.value = str(leftVal + rightVal)
            elif self.operation == "-":
                node.value = str(leftVal - rightVal)
            return node
        return None

    def generateCode(self, llvm):
        return llvm.visitTerm(self)


class FactorNode(Node):
    type = "factor"
    operation = ""
    left = None
    right = None

    def getASTvalue(self):
        return str(self.operation)

    def foldConstant(self):
        if self.left.type == "literal" and self.right.type == "literal":
            node = LiteralNode()
            leftVal = self.left.convertValType()
            rightVal = self.right.convertValType()
            Ltype = self.left.literalType
            Rtype = self.right.literalType
            if Ltype == "float" or Rtype == "float":
                node.literalType = "float"
            else:
                node.literalType = "int"
            if Ltype == "char":
                leftVal = ord(leftVal[1:-1])
            if Rtype == "char":
                temp = rightVal[1:-1]
                rightVal = ord(temp)

            if self.operation == "*":
                node.value = str(leftVal * rightVal)
            elif self.operation == "/":
                if not (leftVal/rightVal).is_integer():
                    node.literalType = "float"
                    node.value = str(leftVal / rightVal)
                else:
                    node.value = str(int(leftVal / rightVal))

            elif self.operation == "%":
                node.value = str(leftVal % rightVal)
            return node
        return None

    def generateCode(self, llvm):
        return llvm.visitFactor(self)


class TypeCastNode(Node):
    type = "cast"
    castTo = ""
    variable = None

    def generateCode(self, llvm):
        return llvm.visitTypeCast(self)


class UnaryNode(Node):
    type = "unary"
    operation = ""
    variable = None

    def getASTvalue(self):
        return str(self.operation)

    def foldConstant(self):
        if self.variable.type == "literal":
            node = LiteralNode()
            val = self.variable.convertValType()
            valType = self.variable.literalType
            if valType == "float":
                node.literalType = "float"
            else:
                node.literalType = "int"
            if valType == "char":
                val = ord(val[1:-1])
            if self.operation == "-":
                node.value = str(-val)
            elif self.operation == "+":
                node.value = str(val)
            elif self.operation == "!":
                node.literalType = "bool"
                node.value = str(not val)
            elif self.operation == "&":
                return None
            return node
        return None

    def generateCode(self, llvm):
        return llvm.visitUnary(self)


class SpecialUnaryNode(Node):
    type = "special_unary"
    operation = ""
    variable = None

    def foldConstant(self):
        if self.variable.type == "literal":
            node = LiteralNode()
            val = self.variable.convertValType()
            valType = self.variable.literalType
            if valType == "bool":
                raise Exception(f"Invalid operation on boolean type")
            elif valType == "float":
                node.literalType = "float"
            else:
                node.literalType = "int"
            if valType == "char":
                val = ord(val[1:-1])
            if self.operation == "--":
                node.value = str(val-1)
            elif self.operation == "++":
                node.value = str(val+1)
            return node
        return None

    def generateCode(self, llvm):
        return llvm.visitSpecialUnary(self)


class LiteralNode(Node):
    type = "literal"
    literalType = ""
    value = ""

    def getASTvalue(self):
        return str(self.value)

    def convertValType(self):
        val = self.value
        if self.literalType == "float":
            val = float(val)
        elif self.literalType == "int":
            val = int(val)
        elif self.literalType == "char":
            val = val[1:-1]
        elif self.literalType == "bool":
            if val == "true" or val == "True":
                val = True
            else:
                val = False
        return val

    def generateCode(self, llvm):
        return llvm.visitLiteral(self)