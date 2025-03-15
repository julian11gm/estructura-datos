class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.siguiente = None

    def __str__(self):
        return f"{self.tipo}: {self.nombre}, {self.edad} años"

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, nombre, edad, tipo):
        nuevo_animal = Animal(nombre, edad, tipo)
        
        if not self.cabeza:
            self.cabeza = nuevo_animal
            print(f"Animal agregado: {nuevo_animal}")
            return
        
        actual = self.cabeza
        while actual.siguiente:
            if actual.nombre == nombre and actual.tipo == tipo:
                print("El animal ya está registrado.")
                return
            actual = actual.siguiente
        
        if actual.nombre == nombre and actual.tipo == tipo:
            print("El animal ya está registrado.")
            return
        
        actual.siguiente = nuevo_animal
        print(f"Animal agregado: {nuevo_animal}")

    def mostrar_animales_iterativo(self):
        if not self.cabeza:
            print("No hay animales registrados.")
            return
        
        actual = self.cabeza
        print("Lista de animales (Iterativo):")
        while actual:
            print(actual)
            actual = actual.siguiente

    def mostrar_animales_recursivo(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
            if nodo is None:
                print("No hay animales registrados.")
                return
            print("Lista de animales (Recursivo):")
        
        print(nodo)
        if nodo.siguiente:
            self.mostrar_animales_recursivo(nodo.siguiente)

    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Agregar un animal")
            print("2. Mostrar animales (Iterativo)")
            print("3. Mostrar animales (Recursivo)")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                nombre = input("Nombre del animal: ")
                edad = int(input("Edad del animal: "))
                tipo = input("Tipo de animal: ")
                self.agregar_animal(nombre, edad, tipo)
            elif opcion == "2":
                self.mostrar_animales_iterativo()
            elif opcion == "3":
                self.mostrar_animales_recursivo()
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intente de nuevo.")

zoo = ListaEnlazada()
zoo.menu()