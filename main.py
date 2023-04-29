import os

from Antlr.CLexer import CLexer
from AstVisitor import *
from AST import AST
from AstOptimizer import AstOptimizer
from LLVMVisitor import LLVMVisitor

# Test script that automatically runs our Compiler on specified C files.
# Just run "python3 main.py"
def main(argv):
    tests_directory_path = "tests/projecten_123_zonder_main/p2"
    ll_directory_path = "tests/ll_files"
    fid = 1
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
            # try:
            #     print("Entering: " + file_path, flush=True)
            #     ast = visitor.visit(tree)
            #     llvm = LLVMVisitor()
            #     llvm.file = ll_directory_path + "/" + filename[0:-2] + ".ll"
            #     ast = optimizer.constantFolding(ast)
            #     ast.generateLLVM(llvm)
            # except Exception as error:
            #     print(error, flush=True)
            if filename == "proj2_opt_pass_typeCast.c":
                print("Entering: " + file_path, flush=True)
                ast = visitor.visit(tree)
                llvm = LLVMVisitor()
                llvm.file = ll_directory_path + "/" + filename[0:-2] + ".ll"
                # if not file_path == "tests/c_files/test_1.txt":
                ast = optimizer.constantFolding(ast)
                ast.generateLLVM(llvm)
                visitor.symbol_table.st_print()

            # ast.vis(fid)
            # fid +=1




if __name__ == '__main__':
    main(sys.argv)
