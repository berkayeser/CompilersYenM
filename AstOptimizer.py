import SymboolTabel
from AST import AST
from Nodes import *


class AstOptimizer:
    st: SymboolTabel

    def optimize(self, tree):
        self.constantPropagation(tree)
        self.constantFolding(tree)

    # We gaan loopen over elke expression en elke identifier vervangen met zijn waarde.
    def constantPropagation(self, tree: AST, st: SymboolTabel):
        self.st = st
        propagated = True
        while propagated:
            propagated = self.constantPropagationRecursive(tree.root)
        return tree

    def constantPropagationRecursive(self, node: Node):
        propagated = False
        for i in range(len(node.children)):
            childNode = node.children[i]
            if childNode.type == "assignment":
                # assignment .right logicexpression/-boolexpression/-term .right factor/element

                if childNode.right.type == "term":
                    """print(childNode.right.type)
                    print( childNode.right.right.type)
                    print( childNode.right.left.type)
                    print()"""

                    # Checken of er een identifier links en/of rechts is
                    # Als de variabele meerdere keren geassigned wordt doen we niets
                    if childNode.right.left.type == "variable" and self.st.get_symbol(childNode.right.left.name)[
                        'value'] is not None and self.st.get_symbol(childNode.right.left.name)['assignOnce'] is True:
                        # identifier vervangen met waarde

                        # 1 waarde opzoeken in symbol table
                        v = self.st.get_symbol(childNode.right.left.name)['value']

                        # 2 nieuwe literal node aanmaken
                        node = LiteralNode()
                        node.value = v
                        nlt = self.st.get_symbol(childNode.right.left.name)['type']
                        if nlt[0:5] == "const":
                            nlt = nlt[5:]
                        node.literalType = nlt
                        # 3 variable node in Term node, vervangen met literal node
                        childNode.right.left = node
                        childNode.right.children[0] = node

                    if childNode.right.right.type == "variable" and self.st.get_symbol(childNode.right.right.name)[
                        'value'] is not None and self.st.get_symbol(childNode.right.right.name)['assignOnce'] is True:
                        v = self.st.get_symbol(childNode.right.right.name)['value']
                        node = LiteralNode()
                        node.value = v
                        nlt = self.st.get_symbol(childNode.right.right.name)['type']
                        if nlt[0:5] == "const":
                            nlt = nlt[5:]
                        node.literalType = nlt
                        childNode.right.right = node
                        childNode.right.children[1] = node


        for child in node.children:
            if self.constantPropagationRecursive(child):
                propagated = True
        return propagated

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
                    if node.type == "unary" or node.type == "special_unary":
                        node.variable = result
                    elif i == 1:
                        node.right = result
                    else:
                        node.left = result
                    folded = True
        for child in node.children:
            if self.constantFoldingRecursive(child):
                folded = True
        return folded
