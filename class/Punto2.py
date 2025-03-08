class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.genero}.")
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_edad(self):
        return self.edad
    def set_edad(self, edad):
        self.edad = edad
    def get_genero(self):
        return self.genero
    def set_genero(self, genero):
        self.genero = genero

class CuentaBancaria:
    def __init__(self, titular, saldo, numero_de_cuenta):
        self.titular = titular
        self.saldo = saldo
        self.numero_de_cuenta = numero_de_cuenta
    def depositar(self, cantidad):
        self.saldo += cantidad
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
    def consultar_saldo(self):
        return self.saldo
    
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)
    def calcular_circunferencia(self):
        return 2 * 3.1416 * self.radio
    
class Libro:
    def __init__(self, titulo, autor, genero, año_de_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año_de_publicacion = año_de_publicacion
    def mostrar_detalles(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año: {self.año_de_publicacion}")

class Cancion:
    def __init__(self, titulo, artista, album, duracion):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion
    def reproducir(self):
        print(f"Reproduciendo: {self.titulo} de {self.artista} ({self.duracion} min)")

class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
    def calcular_total(self, cantidad):
        return self.precio * cantidad
    
class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []
    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)
    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    def esta_aprobado(self):
        return self.calcular_promedio() >= 6
if __name__ == "__main__":
    persona1 = Persona("Julian", 17, "Masculino")
    persona1.presentarse()
    cuenta1 = CuentaBancaria(persona1, 2000, "123456789")
    cuenta1.depositar(700)
    print("Saldo actual:", cuenta1.consultar_saldo())
    rectangulo1 = Rectangulo(12, 6)
    print("Área del rectángulo:", rectangulo1.calcular_area())
    circulo1 = Circulo(8)
    print("Área del círculo:", circulo1.calcular_area())
    libro1 = Libro("1974", "George Orwell", "Fantasia", 1950)
    libro1.mostrar_detalles()
    cancion1 = Cancion("Imagine", "John Lennon", "Imagine", 2.1)
    cancion1.reproducir()
    producto1 = Producto("Laptop", 1500, 6)
    print("Total de compra:", producto1.calcular_total(2))
    estudiante1 = Estudiante("Ana", 20, "Matemáticas")
    estudiante1.agregar_calificacion(12)
    estudiante1.agregar_calificacion(4)
    estudiante1.agregar_calificacion(9)
    print("Promedio del estudiante:", estudiante1.calcular_promedio())
    print("¿Está aprobado?:", estudiante1.esta_aprobado())