import os

from Antlr.CLexer import CLexer
from AstVisitor import *
from AST import AST
from AstOptimizer import AstOptimizer
from LLVMVisitor import LLVMVisitor


def main():
    directory_path = "tests/text_files"
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            if filename == "test_2.c":
                print("Entering: " + file_path)
                input_stream = FileStream(file_path)
                lexer = CLexer(input_stream)
                tokens = CommonTokenStream(lexer)
                parser = CParser(tokens)
                tree = parser.run()

                visitor = AstVisitor()
                ast = AST()
                optimizer = AstOptimizer()

                ast = visitor.visit(tree)

                # visitor.symbol_table.st_print()

                llvm = LLVMVisitor()
                llvm.file = directory_path[0:-10] + "/ll_files/" + filename[0:-1] + "ll"
                # ast = optimizer.constantFolding(ast)

                ast.generateLLVM(llvm)

                ast.vis()


if __name__ == '__main__':
    main()
