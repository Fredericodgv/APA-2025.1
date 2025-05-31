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
    print(f"Fibonacci({n}) iterativo = {fibonacci_iterativo(n)}")
elif opcao == 2:
    print(f"Fibonacci({n}) recursivo = {fibonacci_recursivo(n)}")
else:
    print("Opção inválida!")