import os

from Antlr.CLexer import CLexer
from AstVisitor import *
from AST import AST
from AstOptimizer import AstOptimizer
from LLVMVisitor import LLVMVisitor

# Test script that automatically runs our Compiler on specified C files.
# Just run "python3 main.py"

def main(argv):
    visFlag = True

    if visFlag and 'output' not in os.listdir(): # Als de folder 'output' nog niet bestaat
        os.mkdir('output') # Maak een folder genaamd 'output' aan
        os.mkdir('output/dotfiles') # Maak een folder genaamd 'dotfiles' in 'output' aan

    #c_directory_path = "tests/text_files"

    ll_directory_path = "tests/ll_files"
    #tests_directory_path = "tests/projecten_123_zonder_main"
    tests_directory_path = "tests/projecten_123_zonder_main/p2"

    for filename in os.listdir(tests_directory_path):
        file_path = os.path.join(tests_directory_path, filename)
        if os.path.isfile(file_path):
            input_stream = FileStream(file_path)
            lexer = CLexer(input_stream)
            tokens = CommonTokenStream(lexer)
            parser = CParser(tokens)
            tree = parser.run()

            visitor = AstVisitor()
            optimizer = AstOptimizer()
            try:
                 print("Entering: " + filename, flush=True)
                 ast = visitor.visit(tree)
                 llvm = LLVMVisitor()
                 llvm.file = ll_directory_path + "/" + filename[0:-2] + ".ll"
                 ast = optimizer.constantPropagation(ast, visitor.symbol_table)
                 ast = optimizer.constantFolding(ast)
                 ast.generateLLVM(llvm)

                 if visFlag:
                     ast.vis(filename)
                     visitor.symbol_table.st_print()
            except Exception as error:
                 print(error, flush=True)

        else:
            raise Exception(f"{file_path} not found.")




if __name__ == '__main__':
    main(sys.argv)
