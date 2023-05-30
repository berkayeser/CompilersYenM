from Nodes import *
from MIPSOperations import *

class MIPSVisitor:
    def __int__(self):
        self.file = ""
        self.instructions = list()
        self.symbolTable = dict()
        # block labels
        self.blocks = []
        self.cur_new_label = "L"

    def includeStdio(self):
        pass




    def visitRun(self, node: RunNode):
        if node.include:
            self.includeStdio()
        for child in node.children:
            child.generateMips(self)

        # write result to file
        file = open(self.file, "w")
        for instruction in self.instructions:
            file.write(instruction + '\n')
        file.close()

    def visitIf(self, node: IfNode):
        # First parse Node Condition
        nc = node.condition
        self.cur_new_label = increase_label(self.cur_new_label)
        parsed_nc: str = handle_condition_if(nc, self.cur_new_label) # Parsed Node Condition
        self.instructions.append(nc)

        # Now parse If block
        self.visitBlock(node.block)

        # Now parse Else block
        self.instructions.append(self.cur_new_label)
        if node.elseNode:
            self.visitBlock(node.elseNode.block)


    def visitWhile(self, node: WhileNode):
        condition = node.condition
        condition = self.handle_condition(condition)