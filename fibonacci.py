import time

def main():
    print("Options:")
    print("1. Iterative method")
    print("2. Recursive method")
    choice = input("Choose the method (1/2): ").strip()
    
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a non-negative integer!")
            return
            
        if choice == '1':
            start_time = time.perf_counter()
            result = fibonacci(n)
            end_time = time.perf_counter()
            print(f"The {n}th Fibonacci number is: {result}")
            print(f"Iterative method execution time: {(end_time - start_time)*1000:.6f} milliseconds")
            
        elif choice == '2':
            if n > 35:  # Warning for recursive method
                print("Warning: Recursive method may be slow for n > 35!")
                
            start_time = time.perf_counter()
            result = fibonacci_recursive(n)
            end_time = time.perf_counter()
            print(f"The {n}th Fibonacci number is: {result}")
            print(f"Recursive method execution time: {(end_time - start_time)*1000:.6f} milliseconds")
            
        else:
            print("Invalid choice!")
            
    except ValueError:
        print("Please enter a valid integer!")

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

if __name__ == "__main__":
    main()