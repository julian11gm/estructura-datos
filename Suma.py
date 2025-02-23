def sumar_lista(arr):
    if not arr:
        return 0
    return arr[-1] + sumar_lista(arr[:-1])


numeros = [12, 4, 8, 7, 15, 22]  
resultado = sumar_lista(numeros)
print(f"Suma de la lista: {resultado}")
