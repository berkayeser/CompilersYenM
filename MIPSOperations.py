import struct
from Nodes import *


class Register:
    register = 0
    type = None

    def assign(self, register_nr, type1):
        self.register = register_nr
        self.type = type1

    def load(self, value):
        if self.type == "f":
            return f"li.s $f{self.register}, {value}"
        elif self.type == "s":
            return f"li $s{self.register}, {value}"
        else:
            return f"li $t{self.register}, {value}"


class Local(Register):
    def __init__(self, offset, type):
        self.offset = offset
        self.type = type

    def loadLocal(self, register_nr, sp):
        newRegister = Register()
        if self.type == "float":
            instruction = f"l.s $f{register_nr}, {sp - self.offset}($sp)"
        elif self.type == "byte":
            instruction = f"lb $t{register_nr}, {sp - self.offset}($sp)"
        else:
            instruction = f"lw $t{register_nr}, {sp - self.offset}($sp)"

        return instruction, newRegister.assign(register_nr, self.type)

class Global(Register):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def loadGlobal(self, register_nr):
        newRegister = Register()
        if self.type == "float":
            instruction = f"l.s $f{register_nr}, {self.name}"
        elif self.type == "byte":
            instruction = f"lb $t{register_nr}, {self.name}"
        else:
            instruction = f"lw $t{register_nr}, {self.name}"

        return instruction, newRegister.assign(register_nr, self.type)

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


def add(self, dest, src1, src2):
    if self.type == "f":
        return f"add.s {dest}, {src1}, {src2}"
    elif self.type == "s":
        return f"add {dest}, {src1}, {src2}"
    else:
        return f"addu {dest}, {src1}, {src2}"


def sub(self, dest, src1, src2):
    if self.type == "f":
        return f"sub.s {dest}, {src1}, {src2}"
    elif self.type == "s":
        return f"sub {dest}, {src1}, {src2}"
    else:
        return f"subu {dest}, {src1}, {src2}"


def addi(self, dest, src, immediate):
    if self.type == "f":
        raise ValueError("Cannot perform addi operation on floating-point register")
    elif self.type == "s":
        return f"addi {dest}, {src}, {immediate}"
    else:
        return f"addiu {dest}, {src}, {immediate}"


def subi(self, dest, src, immediate):
    if self.type == "f":
        raise ValueError("Cannot perform subi operation on floating-point register")
    elif self.type == "s":
        return f"subi {dest}, {src}, {immediate}"
    else:
        return f"subiu {dest}, {src}, {immediate}"