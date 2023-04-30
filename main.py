import os

from Antlr.CLexer import CLexer
from AstVisitor import *
from AST import AST
from AstOptimizer import AstOptimizer
from LLVMVisitor import LLVMVisitor

# Test script that automatically runs our Compiler on specified C files.
# Just run "python3 main.py"

def main(argv):
    """if 'output' not in os.listdir(): # Als de folder 'output' nog niet bestaat
        os.mkdir('output') # Maak een folder genaamd 'output' aan

    c_directory_path = "tests/text_files" """

    ll_directory_path = "tests/ll_files"
    tests_directory_path = "tests/projecten_123_zonder_main"
    tests_directory_path = "tests/projecten_123_zonder_main/p1"

    #fid = 1
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
                 ast = optimizer.constantFolding(ast)
                 ast.generateLLVM(llvm)
            except Exception as error:
                 print(error, flush=True)

            # ast.vis(fid)
            # fid +=1

        else:
            raise Exception(f"{file_path} not found.")




if __name__ == '__main__':
    main(sys.argv)
