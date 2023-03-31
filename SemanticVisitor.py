
class SymboolTabel:
    def __init__(self):
        self.scopes = list()
        self.scopes.append(dict())
        self.curScope: int = 0


    def add_symbol(self, name, type, scope=0):
        if name in self.scopes[self.curScope]:
            if self.get_symbol(name)['type'] == type:
                raise Exception(f"Redeclaration: Symbol '{name}' already defined in current scope")
            else:
                raise Exception(f"Redefinition: Symbol '{name}' already defined in current scope")
        else:
            self.scopes[self.curScope][name] = {'type': type, 'scope': scope}
            #self.scopes[-1][name] = {'type': type, 'scope': scope}
            #print(f"{name} , with type {type} added.")
    def get_symbol(self, name, errortype= None):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]

        if errortype == "undef":
            raise Exception(f"Symbol '{name}' is undefined")
        elif errortype == "unint":
            raise Exception(f"Symbol '{name}' is uninitialized")
        else:
            raise Exception(f"Symbol '{name}' is ?????????")


    def open_scope(self):
        self.scopes.append({})

    def sluit_scope(self):
        self.scopes.pop(-1)

    def st_print(self):
        for name, info in self.scopes[0].items():
            print(f"{name} => {info}")
