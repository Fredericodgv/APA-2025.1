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
    print("1. Método Iterativo")
    print("2. Método Recursivo")
    opcao = input("Escolha o método (1/2): ")
    
    try:
        coeficientes = list(map(float, input("Digite os coeficientes (a0 a1 ... an separados por espaço): ").split()))
        x = float(input("Digite o valor de x para avaliação: "))
        
        if not coeficientes:
            print("Lista de coeficientes vazia!")
            return
            
        if opcao == '1':
            resultado = avaliar_polinomio_iterativo(coeficientes, x)
        elif opcao == '2':
            resultado = avaliar_polinomio_recursivo(coeficientes, x)
        else:
            print("Opção inválida!")
            return
            
        print(f"P({x}) = {resultado}")
    except ValueError:
        print("Entrada inválida! Certifique-se de digitar números.")

if __name__ == "__main__":
    main()