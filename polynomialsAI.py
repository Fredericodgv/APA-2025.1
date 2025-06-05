import time

def avaliar_polinomio_iterativo(coeficientes, x):
    """
    Avalia um polinômio usando o método de Horner (iterativo)
    Coeficientes na ordem [a0, a1, a2, ..., an] para a0 + a1*x + a2*x² + ... + an*x^n
    """
    resultado = 0
    for coeficiente in reversed(coeficientes):
        resultado = coeficiente + x * resultado
    return resultado

def avaliar_polinomio_recursivo(coeficientes, x, n=None, resultado_parcial=0):
    """
    Avalia um polinômio recursivamente usando o método de Horner
    Coeficientes na mesma ordem que o iterativo [a0, a1, ..., an]
    """
    if n is None:
        n = len(coeficientes) - 1
    
    if n < 0:
        return resultado_parcial
    
    return avaliar_polinomio_recursivo(
        coeficientes, x, n - 1,
        coeficientes[n] + x * resultado_parcial
    )

def main():
    print("Avaliador de Polinômios")
    print("1. Método Iterativo (Horner)")
    print("2. Método Recursivo (Horner)")
    opcao = input("Escolha o método (1/2): ")
    
    try:
        coeficientes = list(map(float, input("Digite os coeficientes (a0 a1 ... an separados por espaço): ").split()))
        x = float(input("Digite o valor de x para avaliação: "))
        
        if not coeficientes:
            print("Lista de coeficientes vazia!")
            return
            
        if opcao == '1':
            # Medição de tempo para o método iterativo
            inicio = time.perf_counter()
            resultado = avaliar_polinomio_iterativo(coeficientes, x)
            fim = time.perf_counter()
            tempo_iter = (fim - inicio) * 1000  # Convertendo para milissegundos
            
            print(f"\nResultado: P({x}) = {resultado}")
            print(f"Tempo do método iterativo: {tempo_iter:.6f} ms")
            
        elif opcao == '2':
            # Verificação para evitar stack overflow em recursões muito profundas
            if len(coeficientes) > 1000:
                print("\nAviso: Método recursivo pode causar stack overflow para polinômios de grau muito alto!")
                print("Recomendado usar o método iterativo para n > 1000")
                return
            
            # Medição de tempo para o método recursivo
            inicio = time.perf_counter()
            resultado = avaliar_polinomio_recursivo(coeficientes, x)
            fim = time.perf_counter()
            tempo_rec = (fim - inicio) * 1000  # Convertendo para milissegundos
            
            print(f"\nResultado: P({x}) = {resultado}")
            print(f"Tempo do método recursivo: {tempo_rec:.6f} ms")
            
        else:
            print("Opção inválida!")
            
    except ValueError:
        print("Entrada inválida! Certifique-se de digitar números.")
    except RecursionError:
        print("\nErro: Limite de recursão excedido! Use um polinômio de grau menor ou o método iterativo.")

if __name__ == "__main__":
    # Aumentando o limite de recursão para permitir polinômios de grau mais alto
    import sys
    sys.setrecursionlimit(10000)
    main()