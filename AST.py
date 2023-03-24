from Nodes import *
from graphviz import Digraph
import networkx as nx
import networkx.drawing.nx_pydot as nxd
import pydot
class AST:
    root = Node

    def vis(self):
        G = nx.Graph()
        G.add_node("1")
        G.add_node("2")
        G.add_node("3")
        G.add_edge("1", "2")
        G.add_edge("2", "3")
        nxd.write_dot(G, "heere.dot")

        (graph,) = pydot.graph_from_dot_file('heere.dot')
        graph.write_png('somefile.png')


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
