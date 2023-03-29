from AST import AST
from Nodes import *


class AstOptimizer:
    def optimize(self, tree):
        self.constantPropagation(tree)
        self.constantFolding(tree)

    def constantPropagation(self, tree: AST):
        pass

    def constantFolding(self, tree: AST):
        folded = True
        while folded:
            folded = self.constantFoldingRecursive(tree.root)
        return tree

    def constantFoldingRecursive(self, node: Node):
        folded = False
        for i in range(len(node.children)):
            childNode = node.children[i]
            if (childNode.type == "logic" or childNode.type == "compare" or childNode.type == "term"
                    or childNode.type == "factor" or childNode.type == "unary" or childNode.type == "special_unary"):
                result = childNode.foldConstant()
                if result is not None:
                    node.children[i] = result

                    # node has to be an operation node
                    if i == 1:
                        node.right = result
                    else:
                        node.left = result
                    folded = True
        for child in node.children:
            if self.constantFoldingRecursive(child):
                folded = True
        return folded
