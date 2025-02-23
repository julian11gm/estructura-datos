def multiplicacion(a, b):
    if b == 0:
        return 0
    return a + multiplicacion(a, b - 1)

if __name__ == "__main__":
    print(multiplicacion(12, 8))  
    print(multiplicacion(9, 10))