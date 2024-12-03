# Problem Statement 
# Write a function to calculate factorial of a number. 
# Develop a program to compute binomial coefficient (Given N and R).

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def binomial_coefficient(n, r):
    return factorial(n) // (factorial(r) * factorial(n- r))

r=int(input("Enter the value of R: "))

if r > n:
    print("Invalid input: R cannot be greater than N.")
else:
    result = binomial_coefficient(n, r)
    print(f"\nBinomial coefficient c({n}, {r}) = {result}")

