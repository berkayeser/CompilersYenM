from Nodes import *
from graphviz import Digraph
# import networkx as nx
# import networkx.drawing.nx_pydot as nxd
# import pydot
class AST:
    root = Node

    def vis(self):
        pass
        # G = nx.Graph()
        """G.add_node("1")
        G.add_node("2")
        G.add_node("3")
        G.add_edge("+", "3")
        G.add_edge("+", "3")
        G.add_edge("5", "1")
        G.
        G.add_edge("2", "4")"""

        nodes = [self.root]
        #
        # while nodes:
        #     for j in nodes[0].children:
        #         G.add_edge(nodes[0].type, j.type)
        #         nodes.append(j)
        #     nodes.pop(0)
        #
        #
        # #nxd.write_dot(G, "ASTdot.dot")
        # #(graph,) = pydot.graph_from_dot_file('ASTdot.dot')
        #
        # gr = nx.drawing.nx_pydot.to_pydot(G)
        # gr.write_png('ASTpng.png')


        """"
        i = 0
        graph = Digraph()
        graph.node(i.__str__(), self.root.type)
        i += 1
        for node in self.root.children:
            graph.node(i.__str__(), node.type)
            graph.edge("0", i.__str__(), contstraint="false")
            i += 1
        print(graph)"""
