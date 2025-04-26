import pandas as pd

class Directorio:
    def __init__(self,nombre:str, nit:int, sede: str, municipio: str):
        self.nombre = nombre
        self.nit = nit
        self.sede = sede
        self.municipio = municipio

    def __str__(self):
        return f"Nombre: {self.nombre}, NIT:{self.nit}, Sede:{self.sede}, Municipio:{self.municipio}"



class Nodo:
    def __init__(self,Directorio):
        self.Directorio = Directorio
        self.izquierda = None
        self.derecha=None

directorio = pd.read_csv('/workspaces/estructura-datos/excel/Directorio_E.S.E._Hospitales_de_Antioquia_con_coordenadas_20250426 (1).csv')
directorio.rename(columns={'Razón Social Organización': 'nombre',
                           'Número NIT': 'nit',
                           'Nombre Sede': 'sede',
                           'Nombre Municipio':'municipio'}, inplace=True)
print(directorio.head())
print(directorio.dtypes)
directorio['nit']
print(directorio.head())
print(directorio.dtypes)
directorio['nit'] = directorio['nit'].str.replace(',','')
print(directorio.head())
print(directorio.dtypes)
directorio['nit'] = directorio['nit'].astype(int)

print(directorio.columns)
print(directorio['nit'])


for index, row in directorio.iterrows():

    directorio = Directorio(
        nombre=row['nombre'],
        nit=row['nit'],
        sede=row['sede'],
        municipio=row['municipio']
    )
    print(directorio)



        










