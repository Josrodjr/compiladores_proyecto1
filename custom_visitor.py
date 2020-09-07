import antlr4 as antlr4
from antlr_gen.decafLexer import decafLexer
from antlr_gen.decafListener import decafListener
from antlr_gen.decafParser import decafParser
from antlr_gen.decafVisitor import decafVisitor
from antlr4.tree.Trees import Trees
import sys

import codecs

# import the tables we are going to use to check
from tables import Tabla_simbolos, Tabla_tipos, Tabla_ambitos
# import the errors
from errors import Errors

class EvalVisitor(decafVisitor):
    # declare the tables
    t_simbolos = 0
    t_tipos = 0
    t_ambitos = 0

    def __init__(self):
        self.t_simbolos = Tabla_simbolos('Global')
        self.t_tipos = Tabla_tipos()
        self.t_ambitos = Tabla_ambitos()

    # -------------------------------------------- METHOD DECLARATION ---------------------------------------------- 

    # def visitStatement(self, ctx):
        # FIXME: yep cok
 

    def visitVarType(self, ctx):
        # try and get the ID if not return only gettext
        options = ctx.getChildCount()
        # this is a struct
        if options == 2:
            return ctx.getChild(1)
        if options == 1:
            return ctx.getText()

    def visitVarDeclaration(self, ctx):
        # tipo = ctx.varType().getText()
        tipo = str(self.visitVarType(ctx.varType()))
        nombre = ctx.ID().getText()
        arreglo = False
        len_arr = 1
        if ctx.getChildCount() == 6:
            arreglo = True
            len_arr = int(ctx.NUM().getText())
        return [tipo, nombre, arreglo, len_arr]
            

    def visitBlockMETHOD(self, ctx, parent):
        declarations = []

        for value in ctx.varDeclaration():
            declarations.append(self.visitVarDeclaration(value))
        
        # iterate over the declarations inside the method to insert into the symbol table
        for declaration in declarations:
            number_of = 1
            if declaration[2] == False:
                number_of = 1
            if declaration[2] == True:
                number_of = declaration[3]
            # search the table for the type
            tipo = self.t_tipos.search_type(declaration[0])
            # TODO: if -1 raise NON DEFINED VAR
            # serach the ambito for the block
            padre = self.t_ambitos.search_ambito(parent)
            # TODO: if -1 raise NON DEFINED PARENT

            # search the size of the type in the table
            tamanio = self.t_tipos.search_size(tipo)

            self.t_simbolos.create_entry(declaration[1], tipo, padre, tamanio, number_of)

        # for value in ctx.statement():
        #     self.visitStatement(value)
        # FIXME: yep cok

    
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

        parameter_context = ctx.parameter()
        if parameter_context != []:
            for value in parameter_context:
                parameter_list.append(self.visitParameter(value))

        # search the table for the type
        t_tipo = self.t_tipos.search_type(tipo)
        
        # insert into table de ambitos
        self.t_ambitos.create_entry(nombre, 'Program', t_tipo)

        block_context = ctx.block()
        self.visitBlockMETHOD(block_context, nombre)

    # -------------------------------------------- STRUCT DECLARATION ---------------------------------------------- 
    def visitStructDeclaration(self, ctx):
        nombre = ctx.ID().getText()

        vardeclar_context = ctx.varDeclaration()

        if vardeclar_context != []:
            # get the length of variables inside of the struct for memory usage calculation
            n_vars = len(vardeclar_context)

            # insert into the tokens using the values known til now
            self.t_tipos.create_entry(nombre, 4*n_vars, 'definido')
        else:
            line = ctx.start.line
            column = ctx.start.column
            # TODO raise an exeption EMPTY STRUCT

    # -------------------------------------------- BLOCK DECLARATION ---------------------------------------------- 


# def main():
    
#     # abrir el archivo de prueba para tokens
#     with open('test.txt', 'r') as myfile:
#         data = myfile.read()

#     actual_data = antlr4.InputStream(data)
#     # mandar al lexer el input del inpuntstream
#     lexer = decafLexer(actual_data)
#     stream = antlr4.CommonTokenStream(lexer)
#     parser = decafParser(stream)

#     tree = parser.program()

#     # print(Trees.toStringTree(tree, None, parser))

#     answer = EvalVisitor()
    
#     # generate the basic types
#     answer.t_tipos.generate_default_values()
#     # generate the default ambito
#     answer.t_ambitos.generate_default(answer.t_tipos.search_type('void'))

#     # Traverse the tree
#     answer.visit(tree)
    
#     answer.t_simbolos.print_table()
#     answer.t_tipos.print_table()
#     answer.t_ambitos.print_table()

# if __name__ == '__main__':
#     main()