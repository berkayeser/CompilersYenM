class Node:
    children = list()
    type = None
    children = []
    type = "None"
    childrenInit: int = 0

    def addNodes(self, nodes):
        self.children.append(nodes)
        self.childrenInit = 1


class RunNode(Node):
    type = "run"


class LineNode(Node):
    type = "line"
    statement = None
    comment = None


class StatementNode(Node):
    instruction = ""


class CommentNode(Node):
    type = "comment"
    text = ""


class AssignmentNode(Node):
    declaration = None
    expression = None


class InstantiationNode(Node):
    type = ""
    const = False
    name = ""


class VariableNode(Node):
    type = "variable"
    name = ""


class PointerNode(Node):
    type = "pointer"
    name = ""


class CompareNode(Node):
    type = ""
    left = None
    right = None


class TermNode(Node):
    type = ""
    left = None
    right = None


class FactorNode(Node):
    type = ""
    left = None
    right = None


class UnaryNode(Node):
    type = ""
    variable = None


class SpecialUnaryNode(Node):
    type = ""
    variable = None


class LiteralNode(Node):
    type = ""
    value = ""
