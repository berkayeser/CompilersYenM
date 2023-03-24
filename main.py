import sys
from antlr4 import *

from CLexer import CLexer
from CParser import CParser
from AstVisitor import *
from AST import AST
from Nodes import *

def main(argv):
    """"input_stream = FileStream(sys.argv[1])
    lexer = CLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CParser(tokens)
    tree = parser.run()
    visitor = AstVisitor()
    ast = AST()
    ast.root = visitor.visit(tree)
    ast.graphViz()"""
    r = Node()
    ru = RunNode()
    li = LineNode()
    st = StatementNode()
    li.addNodes(st)
    r.addNodes(ru)
    r.addNodes(li)

    b = AST()
    b.root = r
    b.vis()


if __name__ == '__main__':
    main(sys.argv)
