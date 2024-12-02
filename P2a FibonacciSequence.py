# Problem Statement
# Develop a program to generate Fibonacci sequence of length (N). Read N from the console.

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
        
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

n = int(input("Enter the length of the Fibonacci sequence (N): "))

fibonacci_sequence = generate_fibonacci(n)

print(f"\nFibonacci sequence of length {n}:")
print(fibonacci_sequence)

