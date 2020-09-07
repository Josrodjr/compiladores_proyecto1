##Emily Felde, Sam Shissler
##CSCI 468
# Generated from /home/ubuntu/Little.g4 by ANTLR 4.7.1
from antlr4 import *
import collections
if __name__ is not None and "." in __name__:
 from .LittleParser import LittleParser
else:
 from LittleParser import LittleParser
#Not used in final implementation

class SymbolTableBuilder(ParseTreeListener):
    scopes = []
    symbolTables = collections.OrderedDict()
    blockNum = 1
    exprNum = 1
    AST = []
    subTreeRoot = []
    subOldNode = None
    currentNode = None
    oldCurrentNode = None
    currentWrite = []
    inExpr = False
    writeNum = 1
    readNum = 1
    readAndNotWrite = 0
    varType = collections.OrderedDict()

    #enter a new scope, add Dict to AST for new scope
    def enterScope(self, name):
        symbolTable = collections.OrderedDict()
        self.symbolTables[name] = symbolTable
        self.scopes.append(name)
        return name, symbolTable
    
    # create new list for each expression, append it to AST
    def enterAssignExpr(self):
        exprTable = []
        name = "EXPR" + str(self.exprNum)
        self.symbolTables[self.scopes[len(self.scopes)-1]][name] = exprTable
        self.inExpr = True
        return name, exprTable
    
    #leave an expression
    def exitAssignExpr(self):
        self.exprNum +=1
        self.inExpr = False
    
    #leave current scope
    def exitScope(self):
        self.scopes.pop()
    
    #create new block for a scope
    def blockScope(self, blockType):
        name, symbolTable = self.enterScope(blockType)
        self.blockNum+= 1
        return name, symbolTable



# def main():

#     # abrir el archivo de prueba para tokens
#     with open('test.txt', 'r') as myfile:
#         data = myfile.read()

#     actual_data = antlr4.InputStream(data)

#     # mandar al lexer el input del inpuntstream
#     lexer = decafLexer(actual_data)

#     tokens = antlr4.CommonTokenStream(lexer)
#     parser = decafParser(tokens)
#     tree = parser.program()

#     # print the raw tree without formatting
#     # print(tree.toStringTree())

#     # different print of the tree
#     print("HEAR YE! HEAR YE!\n")
#     print(Trees.toStringTree(tree, None, parser))
#     print("\nA message from the king!")

# if __name__ == '__main__':
#     main()



# # generate dummy tables

# test_table = Tabla_simbolos('global')

# test_table.create_entry('value', 0, 'global', 0, 1)
# test_table.create_entry('test', 1, 'global', 8, 1)

# # test_table.print_table()

# test_table2 = Tabla_tipos()

# test_table2.create_entry('string', 8, 'generico')
# test_table2.create_entry('yep', 1, 'struct')

# # test_table2.print_table()

# test_table3 = Tabla_ambitos()

# test_table3.create_entry('Program', 'none', 'class')
# test_table3.create_entry('mystruct', 'none', 'struct')


class Program {
    struct testerino {
        int asdf;
        int asdfas;
    }
    char ayylmao(){
	int works;
    }

    int welp(int yes int no[]) {
        struct testerino meeh;
        char test2[5];
        return test2;
    }
    void help(){
        int test;
        test = 5;
    }
}