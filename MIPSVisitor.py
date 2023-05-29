from Nodes import *
from MIPSOperations import *

class MIPSVisitor:
    def __int__(self):
        self.file = ""
        self.instructions = list()
        self.symbolTable = dict()
        # block labels
        self.blocks = []

    def includeStdio(self):
        pass

    def visitRun(self, node: RunNode):
        if node.include:
            self.includeStdio()
        for child in node.children:
            child.generateAssembly(self)

        # write result to file
        file = open(self.file, "w")
        for instruction in self.instructions:
            file.write(instruction + '\n')
        file.close()
