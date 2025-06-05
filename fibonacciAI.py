import time

def fibonacci_iterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursivo(n, a=0, b=1):
    if n == 0: return a
    return fibonacci_recursivo(n-1, b, a+b)

print("Calculadora de Fibonacci")
print("1. Método Iterativo")
print("2. Método Recursivo")
opcao = int(input("Escolha o método (1 ou 2): "))
n = int(input("Digite o valor de n: "))

if opcao == 1:
    inicio = time.perf_counter()
    resultado = fibonacci_iterativo(n)
    fim = time.perf_counter()
    print(f"Fibonacci({n}) iterativo = {resultado}")
    print(f"Tempo de execução: {(fim - inicio)*1000:.6f} milissegundos")
elif opcao == 2:
    inicio = time.perf_counter()
    resultado = fibonacci_recursivo(n)
    fim = time.perf_counter()
    print(f"Fibonacci({n}) recursivo = {resultado}")
    print(f"Tempo de execução: {(fim - inicio)*1000:.6f} milissegundos")
else:
    print("Opção inválida!")