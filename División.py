def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"
    if a < b:
        return 0
    return 1 + division(a - b, b)


def solicitar_numeros():
    try:
        dividendo = int(input("Ingrese el dividendo: "))
        divisor = int(input("Ingrese el divisor: "))
        resultado = division(dividendo, divisor)
        print(f"{dividendo} dividido entre {divisor} es {resultado}")
    except ValueError:
        print("Error: Ingrese solo números enteros.")


solicitar_numeros()