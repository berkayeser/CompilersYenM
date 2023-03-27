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
# Define the ast_to_dot function
# Define the ast_to_dot function
def ast_to_dot(node):
    # Create a new Digraph object
    dot = graphviz.Digraph()

    # Define a recursive function to visit each node in the AST
    def visit(node, parent=None):
        # Assign a unique ID to the node based on its memory address
        id = str(hash(node))
        # Label the node with its class name
        label = node.getASTvalue()
        dot.node(id, label)

        # Add an edge from the parent node to this node
        if parent:
            dot.edge(parent, id)

        # Recursively visit each child node
        for child in node.children:
            # Node child is another AST node, visit it
            visit(child, id)

    # Call the visit function to traverse the entire AST
    visit(node)

    # Return the DOT code as a string
    return dot.source

def writeDotCode(dot_c):
    dotfilename = 'ast.dot'
    with open(dotfilename, 'w') as f:
        f.write(dot_c)
    (graph,) = pydot.graph_from_dot_file(dotfilename)
    graph.write_png('ASTpng.png')


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

    writeDotCode(ast_to_dot(ast.root))



if __name__ == '__main__':
    main(sys.argv)
