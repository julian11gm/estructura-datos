class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    
    def trabajar(self):
        return f"{self.nombre} está trabajando en el departamento de {self.departamento}."

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo  # Lista de empleados
    
    def trabajar(self):
        return f"{self.nombre} está supervisando a su equipo de {len(self.equipo)} empleados."

    def supervisarAEquipo(self):
        return f"{self.nombre} está supervisando y guiando a su equipo."

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguajeDeProgramacion):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion
    
    def trabajar(self):
        return f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}."
    
    def escribirCodigo(self):
        return f"{self.nombre} está desarrollando software en {self.lenguajeDeProgramacion}."

class FiguraGeométrica:
    def calcularArea(self):
        raise NotImplementedError("Este método debe ser implementado en las subclases")

class Triangulo(FiguraGeométrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeométrica):
    def __init__(self, lado):
        self.lado = lado
    
    def calcularArea(self):
        return self.lado ** 2

class Electrodomestico:
    def __init__(self, marca, modelo, consumoEnergetico):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergetico = consumoEnergetico
    
    def encender(self):
        raise NotImplementedError("Este método debe ser implementado en las subclases")

class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergetico, capacidad):
        super().__init__(marca, modelo, consumoEnergetico)
        self.capacidad = capacidad
    
    def encender(self):
        return f"Lavadora {self.marca} {self.modelo} está iniciando el ciclo de lavado."
    
    def iniciarCicloDeLavado(self):
        return f"Lavadora {self.marca} ha comenzado el lavado con capacidad de {self.capacidad} kg."

class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergetico, tieneCongelador):
        super().__init__(marca, modelo, consumoEnergetico)
        self.tieneCongelador = tieneCongelador
    
    def encender(self):
        return f"Refrigerador {self.marca} {self.modelo} está regulando la temperatura."
    
    def regularTemperatura(self):
        return f"Refrigerador {self.marca} está ajustando la temperatura automáticamente."

class Usuario:
    def __init__(self, nombreDeUsuario, contrasena):
        self.nombreDeUsuario = nombreDeUsuario
        self.contrasena = contrasena
    
    def iniciarSesion(self, usuario, contrasena):
        if self.nombreDeUsuario == usuario and self.contrasena == contrasena:
            return f"Usuario {usuario} ha iniciado sesión con éxito."
        return "Credenciales incorrectas."

class Administrador(Usuario):
    def gestionarUsuarios(self):
        return f"{self.nombreDeUsuario} está gestionando usuarios."

class Cliente(Usuario):
    def realizarCompra(self):
        return f"{self.nombreDeUsuario} está realizando una compra."

if __name__ == "__main__":
    empleado = Empleado("Julian", 12000, "Ventas")
    print(empleado.trabajar())

    gerente = Gerente("Andrea", 78000, "TI", ["Camilo", "Jimena"])
    print(gerente.trabajar())
    print(gerente.supervisarAEquipo())

    desarrollador = Desarrollador("Sofia", 90000, "Desarrollo", "Python")
    print(desarrollador.trabajar())
    print(desarrollador.escribirCodigo())

    triangulo = Triangulo(10, 5)
    print(f"Área del triángulo: {triangulo.calcularArea()}")

    cuadrado = Cuadrado(4)
    print(f"Área del cuadrado: {cuadrado.calcularArea()}")

    lavadora = Lavadora("LG", "TurboWash", "A++", 15)
    print(lavadora.encender())
    print(lavadora.iniciarCicloDeLavado())

    refrigerador = Refrigerador("Samsung", "CoolMax", "A+", True)
    print(refrigerador.encender())
    print(refrigerador.regularTemperatura())

    admin = Administrador("Admin05", "admingod")
    print(admin.iniciarSesion("Admin01", "adminpass"))
    print(admin.gestionarUsuarios())

    cliente = Cliente("Cliente01", "clientegood")
    print(cliente.iniciarSesion("Cliente01", "clientegood"))
    print(cliente.realizarCompra())