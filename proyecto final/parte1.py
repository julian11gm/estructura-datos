# ==============================
#          PILA
# ==============================

class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Agrega un elemento al tope de la pila."""
        self.items.append(item)

    def pop(self):
        """Elimina y devuelve el elemento del tope de la pila."""
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        """Devuelve el elemento del tope sin eliminarlo."""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0

    def size(self):
        """Devuelve el tamaño de la pila."""
        return len(self.items)


# ==============================
#     RECOLECCIÓN DE DATOS
# ==============================
pila_datos = Pila()

def recolectar_datos():
    print("=== Recolección de Datos del Usuario ===")
    
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    peso = input("Peso (kg): ")
    altura = input("Altura (cm): ")
    genero = input("Género (M/F): ")
    
    print("\nSelecciona tu nivel de actividad física:")
    print("1. Sedentario (poco o ningún ejercicio)")
    print("2. Moderado (ejercicio ligero 1-3 días por semana)")
    print("3. Activo (ejercicio moderado 3-5 días por semana)")
    print("4. Muy Activo (ejercicio intenso 6-7 días por semana)")
    
    niveles = {
        "1": "Sedentario",
        "2": "Moderado",
        "3": "Activo",
        "4": "Muy Activo"
    }
    
    nivel_actividad = input("Selecciona el nivel (1-4): ")
    
    # Guardando en la pila
    pila_datos.push(f"Nombre: {nombre}")
    pila_datos.push(f"Edad: {edad}")
    pila_datos.push(f"Peso: {peso} kg")
    pila_datos.push(f"Altura: {altura} cm")
    pila_datos.push(f"Género: {genero}")
    pila_datos.push(f"Nivel de Actividad: {niveles.get(nivel_actividad, 'Desconocido')}")

    print("\n✅ Datos guardados correctamente en la pila.")
    print(f"Tamaño actual de la pila: {pila_datos.size()}")

# Llamada a la función para recolectar los datos
recolectar_datos()


# ==============================
#         CÁLCULO DE TMB
# ==============================

# Diccionario para almacenar los datos del usuario
datos_usuario = {}

def calcular_tmb(pila):
    print("\n=== Cálculo de Tasa Metabólica Basal (TMB) ===")
    
    # Recuperar los datos de la pila y almacenarlos
    datos_usuario["nombre"] = pila.pop().split(": ")[1]
    datos_usuario["edad"] = int(pila.pop().split(": ")[1])
    datos_usuario["peso"] = float(pila.pop().split(": ")[1].split(" ")[0])
    datos_usuario["altura"] = float(pila.pop().split(": ")[1].split(" ")[0])
    datos_usuario["genero"] = pila.pop().split(": ")[1]
    datos_usuario["nivel_actividad"] = pila.pop().split(": ")[1]

    # Cálculo de TMB
    if datos_usuario["genero"].upper() == "M":
        tmb = 10 * datos_usuario["peso"] + 6.25 * datos_usuario["altura"] - 5 * datos_usuario["edad"] + 5
    else:
        tmb = 10 * datos_usuario["peso"] + 6.25 * datos_usuario["altura"] - 5 * datos_usuario["edad"] - 161
    
    # Guardamos el TMB en el diccionario
    datos_usuario["tmb"] = tmb
    
    print(f"TMB calculada para {datos_usuario['nombre']}: {tmb} calorías.")
    return tmb

# Calculamos el TMB
tmb_calculado = calcular_tmb(pila_datos)


# ==============================
#       ÁRBOL BINARIO (BST)
# ==============================

class Nodo:
    def __init__(self, nivel, factor):
        self.nivel = nivel
        self.factor = factor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, nivel, factor):
        """Inserta un nuevo nodo en el árbol."""
        if self.raiz is None:
            self.raiz = Nodo(nivel, factor)
        else:
            self._insertar_recursivo(self.raiz, nivel, factor)

    def _insertar_recursivo(self, nodo_actual, nivel, factor):
        """Inserción recursiva para ubicar el nodo correctamente."""
        if nivel < nodo_actual.nivel:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(nivel, factor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, nivel, factor)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(nivel, factor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, nivel, factor)

    def buscar(self, nivel):
        """Busca un nivel de actividad en el árbol y devuelve su factor."""
        return self._buscar_recursivo(self.raiz, nivel)

    def _buscar_recursivo(self, nodo_actual, nivel):
        """Búsqueda recursiva del nivel en el árbol."""
        if nodo_actual is None:
            return None
        if nodo_actual.nivel == nivel:
            return nodo_actual.factor
        elif nivel < nodo_actual.nivel:
            return self._buscar_recursivo(nodo_actual.izquierda, nivel)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, nivel)

# Instancia y carga del árbol
arbol_niveles = ArbolBinarioBusqueda()
arbol_niveles.insertar("Sedentario", 1.2)
arbol_niveles.insertar("Moderado", 1.375)
arbol_niveles.insertar("Activo", 1.55)
arbol_niveles.insertar("Muy Activo", 1.725)


# ==============================
#       CÁLCULO DE TDEE
# ==============================

def calcular_tdee(tmb, nivel_actividad, arbol):
    print("\n=== Cálculo de Gasto Calórico Total (TDEE) ===")
    factor_actividad = arbol.buscar(nivel_actividad)
    
    if factor_actividad is None:
        print("❌ Error: Nivel de actividad no encontrado en el árbol.")
        return None

    tdee = tmb * factor_actividad
    print(f"Gasto Calórico Total (TDEE): {tdee} calorías.")
    return tdee

# Cálculo final del TDEE
calcular_tdee(tmb_calculado, datos_usuario["nivel_actividad"], arbol_niveles)

