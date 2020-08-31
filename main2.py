from tables import Tabla_simbolos, Tabla_tipos
import tkinter as tk					 
from tkinter import ttk 

# generate dummy tables

test_table = Tabla_simbolos('global')

test_table.create_entry('value', 0, 'global', 0, 1)
test_table.create_entry('test', 1, 'global', 8, 1)

# test_table.print_table()

test_table2 = Tabla_tipos()

test_table2.create_entry('string', 8, 'generico')
test_table2.create_entry('yep', 1, 'struct')

# test_table2.print_table()

# -------------------------------------------- root ---------------------------------------------- 

root = tk.Tk() 
root.title("yep") 
tabControl = ttk.Notebook(root) 
root.geometry("700x600")

tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 

tabControl.add(tab1, text ='Codigo') 
tabControl.add(tab2, text ='Tablas de simbolos') 
tabControl.pack(expand = 1, fill ="both") 

# -------------------------------------------- funcs ---------------------------------------------- 
def save_data(container):
    code_text = container.get('1.0', tk.END)
    # open file to save
    file = open('test.txt', 'w')
    file.write(code_text)


def fill_tables(container):
    simbolos_str = "Tabla de Simbolos \n"
    tipos_str = "Tabla de Tipos \n"
    # scopes_str = "Tabla de scopes \n"

    simbolos_value = test_table.return_table()
    tipos_value = test_table2.return_table()

    # SIMBOLOS
    container.insert(tk.END, simbolos_str)
    container.insert(tk.END, simbolos_value)

    # TIPOS
    container.insert(tk.END, "\n")
    container.insert(tk.END, tipos_str)
    container.insert(tk.END, tipos_value)


# -------------------------------------------- tab1---------------------------------------------- 
code_inserted = tk.Text(tab1)
code_inserted.grid(column=0, row=1)
# open and insert the test code found in the txt
with open('test.txt', 'r') as myfile:
    data = myfile.read()
# insert at the end
code_inserted.insert(tk.END, data)

# insert a button for saving the changes
save_button = tk.Button(tab1, text="Save Changes", command=lambda : save_data(code_inserted) )
save_button.grid(column = 0, row = 2)

# insert a button for new processing
reprocess_button = tk.Button(tab1, text="Reprocess", command=lambda: fill_tables(tables_result) )
reprocess_button.grid(column = 0, row = 3)

# -------------------------------------------- tab2---------------------------------------------- 
# tk.Text(tab2).grid(column = 0 , row = 1) 
tables_result = tk.Text(tab2)
tables_result.grid(column = 0, row = 1)


root.mainloop() 
