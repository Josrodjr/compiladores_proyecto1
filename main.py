import antlr4 as antlr4
from antlr_gen.decafLexer import decafLexer
from antlr_gen.decafListener import decafListener
from antlr_gen.decafParser import decafParser
from antlr4.tree.Trees import Trees
import sys


def main():

    # abrir el archivo de prueba para tokens
    with open('test.txt', 'r') as myfile:
        data = myfile.read()

    actual_data = antlr4.InputStream(data)

    # mandar al lexer el input del inpuntstream
    lexer = decafLexer(actual_data)

    tokens = antlr4.CommonTokenStream(lexer)
    parser = decafParser(tokens)
    tree = parser.program()

    # print the raw tree without formatting
    # print(tree.toStringTree())

    # different print of the tree
    print("HEAR YE! HEAR YE!\n")
    print(Trees.toStringTree(tree, None, parser))
    print("\nA message from the king!")

if __name__ == '__main__':
    main()