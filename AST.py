from Nodes import *
from graphviz import Digraph
import networkx as nx
import networkx.drawing.nx_pydot as nxd
import pydot
import matplotlib.pyplot as plt
import graphviz


class AST:
    root = None

    # Define the visualize function
    def vis(self, fn: str):
        node = self.root
        # Create a new Digraph object
        dot = graphviz.Digraph()

        # Define a recursive function to visit each node in the AST
        def visit(node, parent=None):
            # Assign a unique ID to the node gebaseerd op zijn memory address
            id = str(hash(node))
            # Label the node with its class name
            label = node.getASTvalue()

            if label == "'\x00'":
                label = "/0"
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
        dotfilename = f'tests/output/ast_files/dot_files/{fn}.dot'

        with open(dotfilename, 'w') as f:
            f.write(dot.source)
        # Convert the Dot file to a graphViz graph with Pydot
        (graph,) = pydot.graph_from_dot_file(dotfilename)
        graph.write_png(f'tests/output/ast_files/{fn}.png')

    def generateLLVM(self, llvm):
        self.root.generateCode(llvm)
