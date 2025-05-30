def main():
    print("Options:")
    print("1. Iterative method")
    print("2. Recursive method")
    choice = input("Choose the method (1/2): ").strip()
    n = int(input("Enter a positive integer: "))
    if choice == '1':
        print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    elif choice == '2':
        print(f"The {n}th Fibonacci number is: {fibonacci_recursive(n)}")
    else:
        print("Invalid choice!")

def fibonacci(n):
    for i in range(n + 1):
        if i == 0:
            a, b = 0, 1
        elif i == 1:
            a, b = 1, 1
        else:
            a, b = b, a + b
    
    return a


def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


#Início do programa
if __name__ == "__main__":
    main()

