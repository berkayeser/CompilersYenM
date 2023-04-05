import os

from CLexer import CLexer
from AstVisitor import *
from AST import AST
from AstOptimizer import AstOptimizer
from LLVMVisitor import LLVMVisitor

# Test script that automatically runs our Compiler on specified C files.
# Just run "python3 main.py"
def main(argv):
    directory_path = "tests/text_files"
    fid = 1
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            print("Entering: "+ file_path)
            input_stream = FileStream(file_path)
            lexer = CLexer(input_stream)
            tokens = CommonTokenStream(lexer)
            parser = CParser(tokens)
            tree = parser.run()

            visitor = AstVisitor()
            ast = AST()
            optimizer = AstOptimizer()

            ast.root = visitor.visit(tree)
            # visitor.symbol_table.st_print()

            llvm = LLVMVisitor()
            llvm.file = "tests/ll_files/test_1.ll"
            if not file_path == "tests/text_files/test_1.txt":
                ast = optimizer.constantFolding(ast)
            else:
                ast.generateLLVM(llvm)

            ast.vis(fid)
            fid +=1




if __name__ == '__main__':
    main(sys.argv)
