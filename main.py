import sys
from antlr4 import *

from CLexer import CLexer
from CParser import CParser
from AstVisitor import *
from AST import AST
from Nodes import *
from AstOptimizer import AstOptimizer

def main(argv):
    input_stream = FileStream("example.txt")
    #input_stream = FileStream(sys.argv[1])
    lexer = CLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CParser(tokens)
    tree = parser.run()
    visitor = AstVisitor()
    ast = AST()
    ast.root = visitor.visit(tree)
    optimizer = AstOptimizer()
    ast = optimizer.constantFolding(ast)

    ast.vis()
    for i in ast.root.children:
        print(i.type)
        print(len(i.children))
    for i in ast.root.children[1].children:
        print(i.type)
    optimizer = AstOptimizer()
    ast = optimizer.constantFolding(ast)
    a = 5
    # ast.graphViz()
    # r = Node()
    # ru = RunNode()
    # li = LineNode()
    # st = StatementNode()
    # li.addNodes(st)
    # r.addNodes(ru)
    # r.addNodes(li)
    #
    # b = AST()
    # b.root = r
    # b.vis()


if __name__ == '__main__':
    main(sys.argv)
