class SymbolTable:
    def __init__(self):
        self.scopes = list()
        self.scopes.append(dict())
        self.curScope: int = -1

    def add_symbol(self, name, type):
        s = self.curScope
        if name in self.scopes[s]:
            if self.get_symbol(name)['type'] == type:
                raise Exception(f"Redeclaration: Symbol '{name}' already declared in current scope")
            else:
                raise Exception(f"Redefinition: Symbol '{name}' already defined in current scope")
        else:
            self.scopes[s][name] = {'type': type, 'scope': s, 'value': None, 'assignOnce' : True}

    def symbol_used_twice(self, name:str):
        """
        This function gets called when a symbol has a declaration.
        The symbol then gets marked with 'assignOnce'.
        This is relevant for Constant Propagation.
        :param name: The symbol
        :return:
        """
        self.scopes[self.curScope][name]['assignOnce'] = False

    def add_symbol_value(self, name, value):
        if name not in self.scopes[self.curScope]:
            raise Exception(f"Symbol '{name}' doesnt exist in current scope.")

        self.scopes[self.curScope][name]['value'] = value

    def get_symbol(self, name, errortype=None):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]

        if errortype == "undef":
            raise Exception(f"Semantic Error; Symbol '{name}' is undefined")
        elif errortype == "unint":
            raise Exception(f"Syntax Error; Symbol '{name}' is uninitialized")
        else:
            raise Exception(f"Symbol '{name}' is ?????????")

    def open_scope(self):
        self.scopes.append(dict())

    def close_scope(self):
        self.scopes.pop(-1)

    def st_print(self):
        for i in range(0,len(self.scopes)):
            print(f"Scope {i}:")
            for name, info in self.scopes[i].items():
                print(f"{name} => {info}")
            print()
