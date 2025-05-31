def avaliar_polinomio_iterativo(coeficientes, x):


def avaliar_polinomio_recursivo(coeficientes, x):
    

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