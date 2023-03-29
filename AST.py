from Nodes import *
from graphviz import Digraph
import networkx as nx
import networkx.drawing.nx_pydot as nxd
import pydot
import matplotlib.pyplot as plt
import graphviz

class AST:
    root = Node

    def vis(self):
        self.ast_to_dot(self.root)

    # Define the ast_to_dot function
    def ast_to_dot(self, node):
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
        # return dot.source

        dotfilename = 'ast.dot'
        with open(dotfilename, 'w') as f:
            f.write(dot.source)
        (graph,) = pydot.graph_from_dot_file(dotfilename)
        graph.write_png('ASTpng.png')

