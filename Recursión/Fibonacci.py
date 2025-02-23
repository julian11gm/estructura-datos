def fibonacci_recursivo(n: int, memo=None) -> list:
    if memo is None:
        memo = {0: 0, 1: 1}  
    if n in memo:
        return memo[n] 
    memo[n] = fibonacci_recursivo(n - 1, memo) + fibonacci_recursivo(n - 2, memo)
    return memo[n]
def generar_fibonacci(n: int) -> list:
    return [fibonacci_recursivo(i) for i in range(n)]

n = int(input("Ingrese el número de términos de Fibonacci: "))
print(generar_fibonacci(n)) 