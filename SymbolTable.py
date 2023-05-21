#from AstVisitor import AstVisitor as astvis
class AstVisitor:
    pass

class SymbolTable:
    def __init__(self, name: list[int]):
        """
        self.subscopes; De scopes die in 'deze' scope zitten.
        """
        self.scopes: dict = {} # 1 scope
        self.subScopes: list[SymbolTable] = [] # Children
        self.parentScope: SymbolTable = None
        self.name: list[int] = name

    def add_symbol(self, name, type):
        if name in self.scopes:
            if self.get_symbol(name)['type'] == type:
                #self.st_print()
                raise Exception(f"Redeclaration: Symbol '{name}' already declared in current scope")
            else:
                raise Exception(f"Redefinition: Symbol '{name}' already defined in current scope")
        else:
            self.scopes[name] = {'type': type, 'value': None, 'assignOnce' : True}

    def symbol_used_current(self,name:str):
        if name not in self.scopes:
            return False
        elif self.scopes[name]['value'] is None:
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
        self.scopes[name]['assignOnce'] = False

    def add_symbol_value(self, name, value):
        if name not in self.scopes:
            # instantieren in huidige scope
            symbol = self.get_symbol(name, "undef")
            self.add_symbol(name, symbol['type'])
        self.scopes[name]['value'] = value

    def get_symbol(self, name, errortype=None, input_scope: list[int]=None):
        scope = self
        if input_scope is not None:
            input_scope = input_scope.copy()
            input_scope.pop(0)
            for s in input_scope:
                scope = scope.subScopes[s]
        while scope is not None:
            if name in scope.scopes:
                return scope.scopes[name]
            scope = scope.parentScope

        if errortype == "undef":
            raise Exception(f"Syntax Error; Symbol '{name}' is undefined")
        elif errortype == "unint":
            raise Exception(f"Syntax Error; Symbol '{name}' is uninitialized")
        else:
            self.st_print(True)
            raise Exception(f"Symbol '{name}' is ?????????")

    def open_scope(self, vis: AstVisitor):
        #self.scopes.append(dict())
        #self.curScope += 1
        new_name = self.name.copy()
        new_id = 0 + len(self.subScopes)
        new_name.append(new_id)
        new_st = SymbolTable(new_name)
        new_st.parentScope = self

        self.subScopes.append(new_st)
        vis.cur_symbol_table = new_st

    def close_scope(self, vis: AstVisitor):
        #self.st_print()
        #self.scopes.pop(-1)
        #self.curScope =- 1
        vis.cur_symbol_table = self.parentScope


    def st_print(self, flag = False):
        n = self
        if flag:
            print("*****")

        print(f"Scope {self.name}:")

        if len(self.scopes) == 0:
            print("empty")
        else:
            for name, info in self.scopes.items():
                print(f"{name} => {info}")

        print()
        ""
        for x in n.subScopes:
            print("Subscope: ")
            x.st_print(False)
        if flag:
            print("*___*")

        """for i in range(0,len(self.scopes)):
            print(f"Scope {i}:")
            for name, info in self.scopes[i].items():
                print(f"{name} => {info}")
            print()"""
