import pandas as pd

# Clase Hospital
class Hospital:
    def __init__(self, NIT:int, Organizacion:str, Sede:str, Municipio:str):
        self.NIT = NIT
        self.Organizacion = Organizacion
        self.Sede = Sede
        self.Municipio = Municipio

    def __str__(self):
        return f"NIT: {self.NIT}, Organización: {self.Organizacion}, Sede: {self.Sede}, Municipio: {self.Municipio}"

# Nodo del árbol
class Nodo:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital
        self.izq = None
        self.der = None

# Árbol binario de búsqueda
class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def insertar(self, hospital):
        if self.raiz is None:
            self.raiz = Nodo(hospital)
        else:
            self._insertar(hospital, self.raiz)

    def _insertar(self, hospital, nodo):
        if hospital.NIT < nodo.hospital.NIT:
            if nodo.izq is None:
                nodo.izq = Nodo(hospital)
            else:
                self._insertar(hospital, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodo(hospital)
            else:
                self._insertar(hospital, nodo.der)

    def buscar(self, nit):
        return self._buscar(nit, self.raiz)

    def _buscar(self, nit, nodo):
        if nodo is None:
            return None
        if nit == nodo.hospital.NIT:
            return nodo
        elif nit < nodo.hospital.NIT:
            return self._buscar(nit, nodo.izq)
        else:
            return self._buscar(nit, nodo.der)
        
    def inorden(self):
        
        if self.raiz is not None:
            self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo.izq is not None:
            self._inorden(nodo.izq)
        print(nodo.hospital)
        if nodo.der is not None:
            self._inorden(nodo.der)

# Cargar datos desde el archivo CSV
hospitales = pd.read_csv('/workspaces/estructura-datos/excel/Directorio_E.S.E._Hospitales_de_Antioquia_con_coordenadas_20250426 (1).csv')
hospitales.rename(columns={
    'Número NIT': 'NIT',
    'Razón Social Organización': 'Organizacion',
    'Nombre Sede': 'Sede',
    'Nombre Municipio': 'Municipio'
}, inplace=True)

hospitales['NIT'] = hospitales['NIT'].str.replace(',', '')
hospitales['NIT'] = hospitales['NIT'].astype(int)

# Crear árbol e insertar hospitales
arbol = ArbolBinario()

for index, row in hospitales.iterrows():
    hospital = Hospital(
        NIT=row['NIT'],
        Organizacion=row['Organizacion'],
        Sede=row['Sede'],
        Municipio=row['Municipio'],
    )
    arbol.insertar(hospital)

# Menú
while True:
    print("\n--- MENÚ ---")
    print("1. Buscar hospital por NIT")
    print("2. Recorrido en orden")
    print("3. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        nit = int(input("Ingrese el NIT del hospital: "))
        nodo = arbol.buscar(nit)
        if nodo is not None:
            print("\nHospital encontrado:")
            print(nodo.hospital)
        else:
            print("\nNo se encontró un hospital con ese NIT.")
    
    elif opcion == "2":
        print("\n--- Recorrido en orden ---")
        arbol.inorden()  # Imprime todos los hospitales en orden
    
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida.")