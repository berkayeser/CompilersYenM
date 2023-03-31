from CLexer import CLexer
from AstVisitor import *
from AST import AST
from AstOptimizer import AstOptimizer
from LLVMVisitor import LLVMVisitor

def main(argv):
    input_stream = FileStream("example.txt")
    lexer = CLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CParser(tokens)
    tree = parser.run()

    visitor = AstVisitor()
    ast = AST()
    optimizer = AstOptimizer()

    ast.root = visitor.visit(tree)
    ast = optimizer.constantFolding(ast)

    llvm = LLVMVisitor()
    llvm.file = "example.ll"
    ast.generateLLVM(llvm)

    ast.vis()



if __name__ == '__main__':
    main(sys.argv)
