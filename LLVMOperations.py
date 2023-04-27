class LlvmType:
    def __init__(self, DataType, name, pointer=0):
        self.pointer = pointer
        self.baseType = DataType
        self.name = name
        self.address = False

    def __repr__(self):
        return f"{self.name}"

    @property
    def fullType(self):
        if self.pointer == 0:
            return self.baseType
        else:
            return f"{self.baseType}{'*' * self.pointer}"


# return the signed int to float instruction and the resulting float
def sitofp(name, variable):
    return LlvmType("float", name), f"{name} = sitofp {variable.fullType} {variable} to float"


# return the signed int to float instruction and the resulting float
def fptosi(name, variable):
    return LlvmType("i32", name), f"{name} = fptosi {variable} to i32"


# return the richerThan conversion of variable
def zext(name, variable, to):
    return LlvmType(to, name), f"{name} = zext " + variable.fullType + f" {variable} to {to}"


# return the information losing conversion of variable
def trunc(name, variable, to):
    return LlvmType(to, name), f"{name} = trunc {variable.fullType} {variable} to {to}"


def fcmpLogic(op, name1, name2, name3, var1, var2):
    instruction = [f"{name1} = fcmp one float {var1}, 0.0",
                   f"{name2} = fcmp one float {var2}, 0.0",
                   f"{name3} = {op} i1 {name1}, {name2}"]
    return LlvmType("i1", name3), instruction


def logic(op, name, var1, var2):
    instruction = f"{name} = {op} i1 {var1}, {var2}"
    return LlvmType("i1", name), instruction


def fcmp(op, name, var1, var2):
    return LlvmType("i1", name), f"{name} = fcmp {op} i1 {var1}, {var2}"


def icmp(op, name, var1, var2):
    return LlvmType("i1", name), f"{name} = icmp {op} i1 {var1}, {var2}"


def fadd(name, var1, var2):
    return LlvmType("float", name), f"{name} = fadd float {var1}, {var2}"


def add(name, var1, var2):
    return LlvmType("i32", name), f"{name} = add i32 {var1}, {var2}"


def fsub(name, var1, var2):
    return LlvmType("float", name), f"{name} = fsub float {var1}, {var2}"


def sub(name, var1, var2):
    return LlvmType("i32", name), f"{name} = sub i32 {var1}, {var2}"


def fmul(name, var1, var2):
    return LlvmType("float", name), f"{name} = fmul float {var1}, {var2}"


def mul(name, var1, var2):
    return LlvmType("i32", name), f"{name} = mul i32 {var1}, {var2}"


def fdiv(name, var1, var2):
    return LlvmType("float", name), f"{name} = fdiv float {var1}, {var2}"


def div(name, var1, var2):
    return LlvmType("i32", name), f"{name} = sdiv i32 {var1}, {var2}"


def urem(name, var1, var2):
    return LlvmType("i32", name), f"{name} = urem i32 {var1}, {var2}"


def fneg(name, variable):
    return LlvmType("float", name), f"{name} = fneg float {variable}"


def neg(name, variable):
    return LlvmType("i32", name), f"{name} = neg i32 {variable}"


def xor(name, var1, var2):
    return LlvmType("i1", name), f"{name} = xor i1 {var1}, {var2}"


def alloca(name, DataType, pointer):
    if DataType == "float":
        to = "float"
    elif DataType == "int":
        to = "i32"
    elif DataType == "char":
        to = "i8"
    elif DataType == "bool":
        to = "i1"
    else:
        raise Exception(f"{DataType} is an unsupported Data type")
    variable = LlvmType(to, name)
    variable.pointer = pointer + 1
    return variable, f"{name} = alloca {to + '*' * pointer}"


def load(name, ptr):
    variable = LlvmType(ptr.baseType, name)
    variable.pointer = ptr.pointer-1
    return variable, f"{name} = load {variable.fullType}, {ptr.fullType} {ptr}"


def store(variable, ptr):
    return f"store {variable.fullType} {variable}, {ptr.fullType} {ptr}"
