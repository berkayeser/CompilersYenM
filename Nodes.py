class Node:
    def __int__(self):
        self.children = []
        self.type = None
        self.childrenInit: int = 0

    def addNodes(self, nodes):
        self.children.append(nodes)
        self.childrenInit = 1

    def foldConstant(self):
        return False


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
    declaration = None
    expression = None


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


class TermNode(Node):
    type = "term"
    operation = ""
    left = None
    right = None


class FactorNode(Node):
    type = "factor"
    operation = ""
    left = None
    right = None


class UnaryNode(Node):
    type = "unary"
    operation = ""
    variable = None


class SpecialUnaryNode(Node):
    type = "special_unary"
    operation = ""
    variable = None


class LiteralNode(Node):
    type = "literal"
    literalType = ""
    value = ""
