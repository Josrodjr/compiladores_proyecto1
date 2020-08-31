from tabulate import tabulate

class Tabla_simbolos:
    current_id = 0
    t_name = ''
    t_id = []
    simbolo = []
    location = []
    number_of = []
    tipo = []
    ambito = []

    def __init__(self, name):
        self.t_name = name
        self.current_id = 0
        self.simbolo = []
        self.location = []
        self.number_of = []
        self.tipo = []
        self.ambito = []

    def insert_simbolo(self, s):
        self.simbolo.append(s)

    def insert_tipo(self, t):
        self.tipo.append(t)

    def insert_ambito(self, a):
        self.ambito.append(a)
    
    def insert_location(self, l):
        self.location.append(l)

    def insert_number_of(self, n):
        self.number_of.append(n)

    def assign_id(self):
        self.t_id.append(self.current_id)
        self.current_id = self.current_id + 1

    def create_entry(self, s, t, a, lo, no):
        self.assign_id()
        
        self.insert_simbolo(s)
        self.insert_tipo(t)
        self.insert_ambito(a)

        self.insert_location(lo)
        self.insert_number_of(no)
    
    def print_table(self):
        tabulate_matrix = []
        for i in range(len(self.simbolo)):
            tabulate_matrix.append([self.t_id[i], self.simbolo[i], self.tipo[i], self.ambito[i], self.location[i], self.number_of[i]])
        print('table name: '+self.t_name)
        print(tabulate(tabulate_matrix, headers=['id', 'simbolo', 'tipo', 'ambito', 'location', 'number_of'], tablefmt='github'))

    def return_table(self):
        tabulate_matrix = []
        for i in range(len(self.simbolo)):
            tabulate_matrix.append([self.t_id[i], self.simbolo[i], self.tipo[i], self.ambito[i], self.location[i], self.number_of[i]])
        return tabulate(tabulate_matrix, headers=['id', 'simbolo', 'tipo', 'ambito', 'location', 'number_of'], tablefmt='grid')


class Tabla_tipos:
    current_id = 0
    t_id = []
    nombre = []
    tamanio = []
    tipo = []

    def __init__(self):
        self.current_id = 0
        self.t_id = []
        self.nombre = []
        self.tamanio = []
        self.tipo = []

    def insert_nombre(self, no):
        self.nombre.append(no)

    def insert_tamanio(self, ta):
        self.tamanio.append(ta)

    def insert_tipo(self, ti):
        self.tipo.append(ti)
    
    def assign_id(self):
        self.t_id.append(self.current_id)
        self.current_id = self.current_id + 1

    def create_entry(self, no, ta, ti):
        self.assign_id()

        self.insert_nombre(no)
        self.insert_tamanio(ta)
        self.insert_tipo(ti)
    
    def print_table(self):
        tabulate_matrix = []
        for i in range(len(self.nombre)):
            tabulate_matrix.append([self.t_id[i], self.nombre[i], self.tamanio[i], self.tipo[i]])
        print('table name: Tipos')
        print(tabulate(tabulate_matrix, headers=['id', 'nombre', 'tamaño', 'tipo'], tablefmt='github'))

    def return_table(self):
        tabulate_matrix = []
        for i in range(len(self.nombre)):
            tabulate_matrix.append([self.t_id[i], self.nombre[i], self.tamanio[i], self.tipo[i]])
        return tabulate(tabulate_matrix, headers=['id', 'nombre', 'tamaño', 'tipo'], tablefmt='grid')


    
