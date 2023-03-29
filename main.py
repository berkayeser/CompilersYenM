import sys
from antlr4 import *

from CLexer import CLexer
from CParser import CParser
from AstVisitor import *
from AST import AST
from Nodes import *
from AstOptimizer import AstOptimizer
import pydot
import networkx as nx
import networkx.drawing.nx_pydot as nxd
import graphviz

def main(argv):
    input_stream = FileStream("example.txt")
    #input_stream = FileStream(sys.argv[1])
    lexer = CLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CParser(tokens)
    tree = parser.run()

    visitor = AstVisitor()
    ast = AST()
    optimizer = AstOptimizer()

    ast.root = visitor.visit(tree)
    ast = optimizer.constantFolding(ast)

    ast.vis()



if __name__ == '__main__':
    main(sys.argv)
