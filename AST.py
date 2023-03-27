from Nodes import *
from graphviz import Digraph
import networkx as nx
import networkx.drawing.nx_pydot as nxd
import pydot
import matplotlib.pyplot as plt

class AST:
    root = Node

    def vis(self):
        G = pydot.Dot(graph_type="digraph", strict=True)

        """u = pydot.Node(name="1", label="One")
        v = pydot.Node(name="2", label="One")
        r = pydot.Node(name="3", label="One")
        G.add_node(u)
        G.add_node(v)
        G.add_node(r)
        G.add_edge(pydot.Edge(u,v))
        G.add_edge(pydot.Edge(u,r))"""

        nodes = [self.root]
        id = 0

        while nodes:
            u = pydot.Node(name=id, label=nodes[0].type)
            id += 1
            G.add_node(u)
            #print(nodes[0].type + " en kids: " + str(len(nodes[0].children)))
            for j in nodes[0].children:
                v = pydot.Node(name=id, label=j.type)
                id += 1
                G.add_node(v)
                G.add_edge(pydot.Edge(u,v))
            nodes.pop(0)

        G.write_png('ASTpng.png')

    def vis2(self):
        G = nx.DiGraph()
        nodes = [self.root]

        while nodes:
            print(nodes[0].type + " en kids: " + str(len(nodes[0].children)))
            for j in nodes[0].children:
                G.add_edge(nodes[0].type, j.type)
                nodes.append(j)
            nodes.pop(0)

        # nxd.write_dot(G, "ASTdot.dot")
        # (graph,) = pydot.graph_from_dot_file('ASTdot.dot')
        gr = nx.drawing.nx_pydot.to_pydot(G)
        gr.write_png('ASTpng.png')
