class Node:
    children = list()
    declarationChild = None
    type = None

    def addNodes(self, nodes):
        Node.children.append(nodes)


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


class VariableNode(Node):
    type = "variable"
    value = None


class InstantiationNode(Node):
    type = ""
    const = False
    name = ""


class DeclarationNode(Node):
    type = "="
    name = ""


class CompareNode(Node):
    type = "compare"
    comparison = None


class TermNode(Node):
    type = "+"


class FactorNode(Node):
    type = "*"


class Unary(Node):
    type = "++"
