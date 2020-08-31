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