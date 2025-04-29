# Clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

# Clase Árbol Binario de Búsqueda
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izq, valor)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.der, valor)

    def mostrar_preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=' ')
            self.mostrar_preorden(nodo.izq)
            self.mostrar_preorden(nodo.der)

    def buscar(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self.buscar(nodo.izq, valor)
        else:
            return self.buscar(nodo.der, valor)

# Crear el árbol con los valores dados
valores = [20, 10, 30, 5, 15, 25, 35]
arbol = ArbolBinario()
for v in valores:
    arbol.insertar(v)

# Mostrar el árbol en preorden
print("Árbol en preorden:")
arbol.mostrar_preorden(arbol.raiz)

# Menú de búsqueda
while True:
    print("\n\n--- MENÚ ---")
    print("1. Buscar valor en el árbol")
    print("2. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        entrada = input("Ingrese el valor a buscar: ")
        try:
            valor = int(entrada)
            encontrado = arbol.buscar(arbol.raiz, valor)
            if encontrado:
                print(f"El valor {valor} está en el árbol.")
            else:
                print(f"El valor {valor} NO está en el árbol.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif opcion == "2":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida.")
