import struct
from Nodes import *


class Register:
    register = 0
    type = None

    def assign(self, register_nr, type1):
        self.register = register_nr
        self.type = type1

    def save(self, value, register_nr=0):
        if self.type == "f":
            return f"li $t{register_nr}, {value}\n" \
                   f"mtc1 $t{register_nr}, $f{self.register}"
        elif self.type == "s":
            return f"li $s{self.register}, {value}"
        else:
            return f"li $t{self.register}, {value}"

    def load(self, register_nr=0):
        if self.type == "f":
            return f"mfc1 $t{register_nr}, {self}" \
                   f"l.s {self}, 0($t{register_nr})", self
        return f"lw {self}, 0({self})", self


    def __repr__(self):
        return f"${self.type}{self.register}"


class Local(Register):
    def __init__(self, offset, type):
        self.offset = offset
        self.type = type

    def loadLocal(self, register_nr, sp):
        newRegister = Register()
        if self.type == "float":
            newType = "f"
            instruction = f"l.s $f{register_nr}, {self.offset - sp}($sp)"
        elif self.type == "byte":
            newType = "t"
            instruction = f"lb $t{register_nr}, {self.offset - sp}($sp)"
        else:
            newType = "t"
            instruction = f"lw $t{register_nr}, {self.offset - sp}($sp)"

        return instruction, newRegister.assign(register_nr, newType)

    def storeLocal(self, register, sp):
        if self.type == "float":
            return f"s.s {register}, {self.offset - sp}($sp)"
        else:
            return f"sw {register}, {self.offset - sp}($sp)"

    def loadAddress(self, register_nr, sp):
        newRegister = Register()
        instruction = f"addi $t{register_nr}, $sp, {self.offset - sp}"
        return instruction, newRegister.assign(register_nr, "t")

class Global(Register):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def loadGlobal(self, register_nr):
        newRegister = Register()
        if self.type == "float":
            newType = "f"
            instruction = f"l.s $f{register_nr}, {self.name}"
        elif self.type == "byte":
            newType = "t"
            instruction = f"lb $t{register_nr}, {self.name}"
        else:
            newType = "t"
            instruction = f"lw $t{register_nr}, {self.name}"

        return instruction, newRegister.assign(register_nr, newType)

    def storeGlobal(self, register):
        if self.type == "float":
            return f"s.s {register}, {self.name}"
        else:
            return f"sw {register}, {self.name}"

    def loadAdress(self, register_nr):
        newRegister = Register()
        instruction = f"la $t{register_nr}, {self.name}"
        return instruction, newRegister.assign(register_nr, "t")

class GlobalArray(Register):
    def __init__(self, name, type, size, arraySize):
        self.name = name
        self.type = type
        self.size = size
        self.arraySize = arraySize

    def loadGlobal(self, register_nr, index):
        newRegister = Register()
        if self.type == "float":
            newType = "f"
            instruction = f"l.s $f{register_nr}, {self.name}({index})"
        elif self.type == "byte":
            newType = "t"
            instruction = f"lb $t{register_nr}, {self.name}({index})"
        else:
            newType = "t"
            instruction = f"lw $t{register_nr}, {self.name}({index})"

        return instruction, newRegister.assign(register_nr, newType)

class LocalArray(Register):
    def __init__(self, offset, type, size, arraySize):
        self.offset = offset
        self.type = type
        # size is 1 or 4 (byte or int/float)
        self.size = size
        self.arraySize = arraySize

    def loadLocal(self, register_nr, index):
        newRegister = Register()
        if self.type == "float":
            newType = "f"
            instruction = f"l.s $f{register_nr}, ({index})"
        elif self.type == "byte":
            newType = "t"
            instruction = f"lb $t{register_nr}, ({index})"
        else:
            newType = "t"
            instruction = f"lw $t{register_nr}, ({index})"

        return instruction, newRegister.assign(register_nr, newType)

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
        print("error151")

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
            print("error174" + str(operator))

        return [string]


# Parse a string for Printf
def parse_string(string: str, argument: list[ArgumentNode]) -> str:
    parsed: str = "\""

    ctr: int = 0
    for i in range(0, len(string)):
        if string[i-1] == "%":
            continue
        if string[i] == "%":
            a = argument[ctr].value
            if isinstance(a, str):
                parsed += a
            elif a.type == "literal":
                parsed += a.value
            elif a.type == "variable":
                print("errorVar")
            else:
                print("errorElse")
            ctr += 1
        else:
            parsed += string[i]
    parsed += "\""
    return parsed


def float_to_64bit_hex(x):
    if isinstance(x, str):
        x = float(x)
    bytes_of_x = struct.pack('>f', x)
    x_as_int = struct.unpack('>f', bytes_of_x)[0]
    x_as_double = struct.pack('>d', x_as_int).hex()
    x_as_double = '0x' + x_as_double
    return x_as_double


def add(dest, src1, src2):
    if dest.type == "f":
        return f"add.s {dest}, {src1}, {src2}"
    elif dest.type == "s":
        return f"add {dest}, {src1}, {src2}"
    else:
        return f"addu {dest}, {src1}, {src2}"


def sub(dest, src1, src2):
    if dest.type == "f":
        return f"sub.s {dest}, {src1}, {src2}"
    elif dest.type == "s":
        return f"sub {dest}, {src1}, {src2}"
    else:
        return f"subu {dest}, {src1}, {src2}"


def addi(dest, src, immediate):
    if dest.type == "f":
        raise ValueError("Cannot perform addi operation on floating-point register")
    elif dest.type == "s":
        return f"addi {dest}, {src}, {immediate}"
    else:
        return f"addiu {dest}, {src}, {immediate}"


def subi(dest, src, immediate):
    if dest.type == "f":
        raise ValueError("Cannot perform subi operation on floating-point register")
    elif dest.type == "s":
        return f"subi {dest}, {src}, {immediate}"
    else:
        return f"subiu {dest}, {src}, {immediate}"


def convert_float_to_int(dest, src):
    return f"cvt.w.s {dest}, {src}"


def convert_int_to_float(dest, src):
    return f"cvt.s.w {dest}, {src}"


def neg(dest, src):
    if dest.type == "f":
        return f"neg.s {dest}, {src}"
    else:
        return f"neg {dest}, {src}"


def logical_not(dest, src):
    return f"xori {dest}, {src}, 1"


def multiply(dest, src1, src2):
    if dest.type == "f":
        return f"mul.s {dest}, {src1}, {src2}"
    else:  # Assuming data_type is "int"
        return f"mul {dest}, {src1}, {src2}"


def divide(dest, src1, src2):
    if dest.type == "f":
        return f"div.s {src1}, {src2}\n" \
               f"mov.s {dest}, $f0"
    else:  # Assuming data_type is "int"
        return f"div {src1}, {src2}\n" \
               f"mflo {dest}"


def modulo(dest, src1, src2):
    if dest.type == "f":
        return f"rem.s {src1}, {src2}\n" \
               f"mov.s {dest}, {src1}"
    else:  # Assuming data_type is "int"
        return f"div {src1}, {src2}\n" \
               f"mfhi {dest}"


# assuming one is stored in temp
def compare(dest, op, src1, src2, temp=None):
    if dest.type == "f":
        instruction = ""
        if op == "<":
            instruction = f"c.lt.s {src1}, {src2}\n" \
                   f"movf {temp}, $zero"
        elif op == ">":
            instruction = f"c.lt.s {src2}, {src1}\n" \
                   f"movf {temp}, $zero"
        elif op == "<=":
            instruction = f"c.le.s {src1}, {src2}\n" \
                   f"movf {temp}, $zero"
        elif op == ">=":
            instruction = f"c.le.s {src2}, {src1}\n" \
                   f"movf {temp}, $zero"
        elif op == "==":
            instruction = f"c.eq.s {src1}, {src2}\n" \
                   f"movf {temp}, $zero"
        elif op == "!=":
            instruction = f"c.eq.s {src1}, {src2}\n" \
                   f"movt {temp}, $zero"
        else:
            raise ValueError("Invalid comparison operator")
        instruction += f"\nmtc1 {temp}, {src1}"
        return instruction
    else:
        if op == "<":
            return f"slt {dest}, {src1}, {src2}"
        elif op == ">":
            return f"slt {dest}, {src2}, {src1}"
        elif op == "<=":
            return f"slt {dest}, {src2}, {src1}\n" \
                   f"xori {dest}, {dest}, 1"
        elif op == ">=":
            return f"slt {dest}, {src1}, {src2}\n" \
                   f"xori {dest}, {dest}, 1"
        elif op == "==":
            return f"seq {dest}, {src1}, {src2}"
        elif op == "!=":
            return f"sne {dest}, {src1}, {src2}"
        else:
            raise ValueError("Invalid comparison operator")


# no flaots
def logical_and(dest, src1, src2):
        return f"and $t{dest}, $t{src1}, $t{src2}"


# no floats
def logical_or(dest, src1, src2):
        return f"or $t{dest}, $t{src1}, $t{src2}"
