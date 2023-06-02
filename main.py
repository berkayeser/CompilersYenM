import os

from Antlr.CLexer import CLexer
from AstVisitor import *
from AST import AST
from AstOptimizer import AstOptimizer
from LLVMVisitor import LLVMVisitor
from MIPSVisitor import *

# Test script that automatically runs our Compiler on specified C files.
# Just run "python3 main.py"

def main(argv):
    vis_tree_flag: bool = True
    vis_st_flag: bool = False

    if 'output' not in os.listdir('tests'):  # Als de folder 'output' nog niet bestaat
        os.mkdir('tests/output')  # Maak een folder genaamd 'output' aan
    if 'asm_files' not in os.listdir('tests/output'):  # Als de folder 'asm' nog niet bestaat
        os.mkdir('tests/output/asm_files')  # Maak een folder genaamd 'asm' aan
    if vis_tree_flag and 'ast_files' not in os.listdir('tests/output'): # Als de folder 'output' nog niet bestaat
        os.mkdir('tests/output/ast_files') # Maak een folder genaamd 'output' aan
        os.mkdir('tests/output/ast_files/dot_files') # Maak een folder genaamd 'dotfiles' in 'output' aan

    tests_directory_path = "tests/alle_projecten"
    asm_directory_path = "tests/output/asm_files"

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
                try:
                    print("Entering: " + filename, flush=True)
                    ast = visitor.visit(tree)
                    ast = optimizer.optimize(ast, visitor.symbol_table)

                    if vis_tree_flag:
                        ast.vis(filename)
                    if vis_st_flag:
                        visitor.symbol_table.st_print(True)

                    mips = MIPSVisitor()
                    mips.file = asm_directory_path + "/" + filename[0:-2] + ".asm"
                    ast.generateMips(mips)

                except Exception as error:
                     print(error, flush=True)

                print(flush=True)
            else:
                raise Exception(f"{file_path} not found.")


if __name__ == '__main__':
    main(sys.argv)
