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

    if 'output' not in os.listdir('tests'):  # Als de folder 'll' nog niet bestaat
        os.mkdir('tests/output')  # Maak een folder genaamd 'output' aan
    #if 'll_files' not in os.listdir('tests/output'):  # Als de folder 'll' nog niet bestaat
    #    os.mkdir('tests/output/ll_files')  # Maak een folder genaamd 'll' aan
    if visFlag and 'ast_files' not in os.listdir('tests/output'): # Als de folder 'output' nog niet bestaat
        os.mkdir('tests/output/ast_files') # Maak een folder genaamd 'output' aan
        os.mkdir('tests/output/ast_files/dot_files') # Maak een folder genaamd 'dotfiles' in 'output' aan

    #c_directory_path = "tests/text_files"
    #ll_directory_path = "tests/output/ll_files"
    #tests_directory_path = "tests/projecten_123_zonder_main"
    #tests_directory_path = "tests/alle_projecten"
    tests_directory_path = "tests/projecten_4"

    for foldername in os.listdir(tests_directory_path):
        print(f"\nEntering project {foldername}. \n")
        foldername = os.path.join(tests_directory_path, foldername)
        for filename in os.listdir(foldername):
            file_path = os.path.join(foldername, filename)

            if os.path.isfile(file_path):
                input_stream = FileStream(file_path)
                lexer = CLexer(input_stream)
                tokens = CommonTokenStream(lexer)
                parser = CParser(tokens)
                parser.removeErrorListeners()
                tree = parser.run()

                visitor = AstVisitor()
                optimizer = AstOptimizer()
                #try:
                print("Entering: " + filename, flush=True)
                ast = visitor.visit(tree)
                #llvm = LLVMVisitor()
                #llvm.file = ll_directory_path + "/" + filename[0:-2] + ".ll"
                ast = optimizer.optimize(ast, visitor.symbol_table)

                if visFlag:
                    ast.vis(filename)
                    visitor.symbol_table.st_print()

                    #ast.generateLLVM(llvm)
                #except Exception as error:
                #     print(error, flush=True)
            else:
                raise Exception(f"{file_path} not found.")


if __name__ == '__main__':
    main(sys.argv)
