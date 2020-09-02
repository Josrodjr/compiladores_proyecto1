import antlr4 as antlr4
from antlr_gen.decafLexer import decafLexer
from antlr_gen.decafListener import decafListener
from antlr_gen.decafParser import decafParser
from antlr_gen.decafVisitor import decafVisitor
from antlr4.tree.Trees import Trees
import sys

import codecs


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

class EvalVisitor(decafVisitor):

    # def visitStatement(self, ctx):
        # TODO: yep cok
        
        
    def visitVarDeclaration(self, ctx):
        tipo = ctx.varType().getText()
        nombre = ctx.ID().getText()
        arreglo = False
        len_arr = 1
        if ctx.getChildCount() == 6:
            arreglo = True
            len_arr = int(ctx.NUM().getText())
        return (tipo, nombre, arreglo, len_arr)
            

    def visitBlockMETHOD(self, ctx, parent):
        declarations = []

        for value in ctx.varDeclaration():
            declarations.append(self.visitVarDeclaration(value))
        
        # for value in ctx.statement():
        #     self.visitStatement(value)
        # TODO: yep cok

    
    def visitParameter(self, ctx):
        tipo = ctx.parametertype().getText()
        nombre = ctx.ID().getText()
        arreglo = False
        if ctx.getChildCount() == 4:
            arreglo = True
        return(tipo, nombre, arreglo)
        


    def visitMethoDeclaration(self, ctx):
        tipo = ctx.methodType().getText()
        nombre = ctx.ID().getText()
        parameter_list = []
        # print(ctx.methodType().getText())
        # print(ctx.ID())
        parameter_context = ctx.parameter()
        if parameter_context != []:
            for value in parameter_context:
                parameter_list.append(self.visitParameter(value))
        
        block_context = ctx.block()
        self.visitBlockMETHOD(block_context, nombre)


        # print(tipo, nombre, parameter_list)




def main():
    
    # abrir el archivo de prueba para tokens
    with open('test.txt', 'r') as myfile:
        data = myfile.read()

    actual_data = antlr4.InputStream(data)
    # mandar al lexer el input del inpuntstream
    lexer = decafLexer(actual_data)
    stream = antlr4.CommonTokenStream(lexer)
    parser = decafParser(stream)

    tree = parser.program()

    # print(Trees.toStringTree(tree, None, parser))

    answer = EvalVisitor().visit(tree)

if __name__ == '__main__':
    main()