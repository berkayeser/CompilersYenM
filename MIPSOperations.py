import struct
from Nodes import *

class Local:
    def __init__(self, offset, type):
        self.register = 0
        self.offset = offset
        self.type = type

    def load(self, sp):
        if self.type == "float":
            return f"l.s $f{self.register}, {sp - self.offset}($sp)"
        else:
            return f"lw $t{self.register}, {sp - self.offset}($sp)"


class Global:
    def __init__(self, name, type):
        self.register = 0
        self.name = name
        self.type = type

    def load(self, sp):
        if self.type == "float":
            return f"l.s $f{self.register}, {self.name}"
        else:
            return f"lw $t{self.register}, {self.name}"


class Temp:
    def __init__(self, value, type):
        self.register = 0
        self.value = value
        self.type = type

    def load(self, sp):
        if self.type == "float":
            return f"li.s $f{self.register}, {self.value}"
        else:
            return f"li $t{self.register}, {self.value}"



def handle_condition(self ,var1, var2, operator :str) -> str:
    string :str = ""
    if operator   == "==":
        string = "beq $t0, $t1, then"
    elif operator == "!=":
        string = "bne $t0, $t1, then"
    elif operator == "<":
        string = "blt $t0, $t1, then"
    elif operator == ">":
        string = "bgt $t0, $t1, then"
    elif operator == "<=":
        string = "ble $t0, $t1, then"
    elif operator == ">=":
        string = "bge $t0, $t1, then"
    else:
        print("error")

    return string


def handle_condition_if(operator:str, label:str) -> list[str]:
        # Assumes the condition variables, are in $t0 and $t1
        # For an If loop, we need to reverse the condition
        string:str = ""

        if operator   == "==":
            string = "bne $t0, $t1, " + label
        elif operator == "!=":
            string = "beq $t0, $t1, " + label
        elif operator == "<":
            string = "bge $t0, $t1, " + label
        elif operator == ">":
            string = "ble $t0, $t1, " + label
        elif operator == "<=":
            string = "bgt $t0, $t1, " + label
        elif operator == ">=":
            string = "blt $t0, $t1, " + label
        else:
            print("error")

        return [string]

def float_to_64bit_hex(x):
    if isinstance(x, str):
        x = float(x)
    bytes_of_x = struct.pack('>f', x)
    x_as_int = struct.unpack('>f', bytes_of_x)[0]
    x_as_double = struct.pack('>d', x_as_int).hex()
    x_as_double = '0x' + x_as_double
    return x_as_double

def convertNode(node: LiteralNode):
    value = node.convertValType()
    nlt = str(node.literalType)
    if nlt == "int":
        return Temp(value, "word")
    elif nlt == "float":
        return Temp(float_to_64bit_hex(value), "float")
    elif nlt == "char":
        return Temp(value, "byte")
    elif nlt == "bool":
        if value:
            return Temp(1, "word")
        return Temp(0, "word")
    raise Exception(f"Node Literal Type '{nlt}' not supported")

