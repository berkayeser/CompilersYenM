#from AstVisitor import AstVisitor as astvis
class astvis:
    pass

class SymbolTable:
    """
    [
    {..., nested Subscopes = [{},{},{}]},
    {},
    {},
    ]
    """
    def __init__(self):
        """
        self.subscopes; De scopes die in 'deze' scope zitten.
        """
        self.scopes: list[dict] = [{}]
        #self.scopes: dict = {}
        self.curScope: int = 0
        self.subScopes: list[SymbolTable] = [] # Children
        self.parentScope: SymbolTable = None

    def add_symbol(self, name, type):
        s = self.curScope
        if name in self.scopes[s]:
            if self.get_symbol(name)['type'] == type:
                #self.st_print()
                raise Exception(f"Redeclaration: Symbol '{name}' already declared in current scope")
            else:
                raise Exception(f"Redefinition: Symbol '{name}' already defined in current scope")
        else:
            self.scopes[s][name] = {'type': type, 'value': None, 'assignOnce' : True}

    def symbol_used_current(self,name:str):
        if name not in self.scopes[self.curScope]:
            return False
        elif self.scopes[self.curScope][name]['value'] is None:
            return False
        else:
            return True

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
            # instantieren in huidige scope
            symbol = self.get_symbol(name, "undef")
            self.add_symbol(name, symbol['type'])
        self.scopes[self.curScope][name]['value'] = value

    def get_symbol(self, name, errortype=None):
        """for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]"""
        scope = self
        while scope is not None:
            if name in scope.scopes[0]:

                return scope.scopes[0][name]
            scope = scope.parentScope
        if errortype == "undef":
            raise Exception(f"Syntax Error; Symbol '{name}' is undefined")
        elif errortype == "unint":
            raise Exception(f"Syntax Error; Symbol '{name}' is uninitialized")
        else:
            raise Exception(f"Symbol '{name}' is ?????????")

    def open_scope(self, vis:astvis):
        #self.scopes.append(dict())
        #self.curScope += 1
        new_st = SymbolTable()
        self.subScopes.append(new_st)
        new_st.parentScope = self
        vis.cur_symbol_table = new_st

    def close_scope(self, vis:astvis):
        #self.st_print()
        #self.scopes.pop(-1)
        #self.curScope =- 1
        vis.cur_symbol_table = self.parentScope


    def st_print(self):
        n = self
        i = 0
        print(f"Scope {i}:")
        for name, info in self.scopes[i].items():
            print(f"{name} => {info}")
        print()
        ""
        for x in n.subScopes:
            print("Subscope: ")
            x.st_print()

        """for i in range(0,len(self.scopes)):
            print(f"Scope {i}:")
            for name, info in self.scopes[i].items():
                print(f"{name} => {info}")
            print()"""
