from AST import AST
from Nodes import *


class AstOptimizer:
    def constantFolding(self, tree: AST):
        folded = True
        while folded:
            folded = self.constantFoldingRecursive(tree.root)
        return tree

    def constantFoldingRecursive(self, node: Node):
        folded = False
        if (node.type == "compare" or node.type == "term" or node.type == "factor"
                or node.type == "unary" or node.type == "special_unary"):
            folded = node.foldConstant()
        for child in node.children:
            self.constantFoldingRecursive(child)
        return folded
