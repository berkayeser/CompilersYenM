class Node:
    children = []
    type = None
    childrenInit: int = 0

    def __init__(self):
        self.children = []

    def addNodes(self, nodes):
        self.children.append(nodes)
        self.childrenInit = 1

    def foldConstant(self):
        return None


class RunNode(Node):
    type = "run"


class LineNode(Node):
    type = "line"
    statement = None
    comment = None


class StatementNode(Node):
    type = "statement"
    instruction = ""


class CommentNode(Node):
    type = "comment"
    text = ""


class AssignmentNode(Node):
    type = "assignment"
    left = None
    right = None


class InstantiationNode(Node):
    type = "instantiation"
    varType = ""
    const = False
    name = ""


class VariableNode(Node):
    type = "variable"
    name = ""


class PointerNode(Node):
    type = "pointer"
    name = ""


class CompareNode(Node):
    type = "compare"
    operation = ""
    left = None
    right = None

    def foldConstant(self):
        if self.left.type == "literal" and self.right.type == "literal":
            node = LiteralNode()
            leftVal = self.left.converValType()
            rightVal = self.right.converValType()
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


class TermNode(Node):
    type = "term"
    operation = ""
    left = None
    right = None

    def foldConstant(self):
        if self.left.type == "literal" and self.right.type == "literal":
            node = LiteralNode()
            leftVal = self.left.convertValType()
            rightVal = self.right.convertValType()
            Ltype = self.left.literalType
            Rtype = self.right.literalType
            if Ltype == "string" or Rtype == "string":
                return None
            elif Ltype == "float" or Rtype == "float":
                node.literalType = "float"
            else:
                node.literalType = "int"
            if Ltype == "char":
                leftVal = ord(leftVal[1:-1])
            if Rtype == "char":
                temp = rightVal[1:-1]
                rightVal = ord(temp)

            if self.operation == "+":
                node.value = leftVal + rightVal
            elif self.operation == "-":
                node.value = leftVal - rightVal
            return node
        return None


class FactorNode(Node):
    type = "factor"
    operation = ""
    left = None
    right = None

    def foldConstant(self):
        if self.left.type == "literal" and self.right.type == "literal":
            node = LiteralNode()
            leftVal = self.left.convertValType()
            rightVal = self.right.convertValType()
            Ltype = self.left.literalType
            Rtype = self.right.literalType
            if Ltype == "string" or Rtype == "string":
                return None
            elif Ltype == "float" or Rtype == "float":
                node.literalType = "float"
            else:
                node.literalType = "int"
            if Ltype == "char":
                leftVal = ord(leftVal[1:-1])
            if Rtype == "char":
                temp = rightVal[1:-1]
                rightVal = ord(temp)

            if self.operation == "*":
                node.value = leftVal * rightVal
            elif self.operation == "/":
                node.value = leftVal / rightVal
            elif self.operation == "%":
                node.value = leftVal % rightVal
            return node
        return None


class UnaryNode(Node):
    type = "unary"
    operation = ""
    variable = None

    def foldConstant(self):
        if self.variable.type == "literal":
            node = LiteralNode()
            val = self.variable.convertValType()
            valType = self.variable.literalType
            if valType == "string":
                return None
            elif valType == "float":
                node.literalType = "float"
            else:
                node.literalType = "int"
            if valType == "char":
                val = ord(val[1:-1])
            if self.operation == "-":
                node.value = -val
            elif self.operation == "!":
                node.literalType = "bool"
                node.value = not val
            elif self.operation == "&":
                return None
            return node
        return None


class SpecialUnaryNode(Node):
    type = "special_unary"
    operation = ""
    variable = None

    def foldConstant(self):
        if self.variable.type == "literal":
            node = LiteralNode()
            val = self.variable.convertValType()
            valType = self.variable.literalType
            if valType == "string" or valType == "bool":
                return None
            elif valType == "float":
                node.literalType = "float"
            else:
                node.literalType = "int"
            if valType == "char":
                val = ord(val[1:-1])
            if self.operation == "--":
                node.value = val-1
            elif self.operation == "++":
                node.value = val+1
            return node
        return None


class LiteralNode(Node):
    type = "literal"
    literalType = ""
    value = ""

    def convertValType(self):
        val = self.value
        if self.literalType == "int":
            val = int(val)
        elif self.literalType == "float":
            val = float(val)
        elif self.literalType == "bool":
            if val == "true":
                val = True
            else:
                val = False
        return val
