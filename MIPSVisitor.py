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

    def increase_label(self):
        integer = int(self.cur_new_label[1:])
        self.cur_new_label = "L" + str(integer + 1)

    def visitIf(self, node: IfNode):
        self.increase_label()
        else_label = self.cur_new_label

        # First parse Node Condition
        nc = node.condition
        #TODO De TermNode in de condition nog omzetten naar MIPS
        parsed_nc: list[str] = handle_condition_if(nc, else_label) # Parsed Node Condition

        # nc = Als de conditie niet waar is, springen we over het 'if' block:

        for i in parsed_nc:
            self.instructions.append(i)

        # Now parse If block
        self.visitBlock(node.block)

        # Als er een 'else' is, hierover heen springen
        else_node = False
        if node.elseNode:
            else_node = True
            self.increase_label()
            next_label: str = self.cur_new_label
            self.instructions.append("j " + next_label)

        # Now parse Else block
        self.instructions.append(else_label + ": ")
        if else_node:
            self.visitBlock(node.elseNode.block)


    def visitWhile(self, node: WhileNode):
        condition = node.condition
        block = node.block

        # Start of While block
        self.increase_label()
        while_label: str = self.cur_new_label
        self.instructions.append(while_label + ": ")

        # Parse Condition
        self.increase_label()
        done_label: str = self.cur_new_label
        parsed_condition = handle_condition_if(condition, done_label)

        for i in parsed_condition:
            self.instructions.append(i)

        # Parse While block
        self.visitBlock(block)

        # At end of while block, jump back to begin of While
        self.instructions.append("j "+ while_label )

