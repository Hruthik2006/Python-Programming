# Problem Statement
# Design a basic calculator that can perform addition, subtraction, multiplication, and division. 
# Extend it to handle more complex operations like square roots, exponents, and trigonometric functions.

import math

def basic_operations():
    print("\n--- Basic Operations ---")
    num1 float(input("Enter the first number: "))
    operator = input("Enter the operation (+, -, *, /): ")
    num2= float(input("Enter the second number: "))
    if operator == '+':
        result = num1 num2
    elif operator == '-':
        result num1 num2
    elif operator == '*':
        result num1 num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is undefined."
    else:
        result = "Invalid operation"
        
    print(f"Result: (result)")
    
def advanced_operations():
    print("\n- Advanced Operations")
    print("1. Square Root")
    print("2. Exponentiation")
    print("3. Sine")
    print("4. Cosine")
    print("5. Tangent")
    choice = int(input("Choose an operation (1-5): "))
    
    if choice 1:
        num= float(input("Enter the number: "))
        result math.sqrt(num)
        print(f"Square Root of (num) is (result)")
    elif choice 2:
        base float(input("Enter the base: "))
        exp= float(input("Enter the exponent: "))
        result math.pow(base, exp)
        print (f"(base) raised to the power of (exp) is (result)")
    elif choice == 3:
        angle float(input("Enter the angle in degrees: "))
        result math.sin(math.radians (angle))
        print(f"Sine of (angle) degrees is (result)")
    elif choice as 4:
        angle float(input("Enter the angle in degrees: "))
        result math.cos(math.radians (angle))
        print(f"Cosine of (angle) degrees is (result)")
    elif choice = 5:
        angle float(input("Enter the angle in degrees: "))
        result = math.tan(math.radians (angle))
        print(f"Tangent of (angle) degrees is (result)")
    else:
        print("Invalid choice")

while True:
    print("\n--- Calculator---")
    print("1. Basic Operations")
    print("2. Advanced Operations")
    print("3. Exit")
    choice int(input("Choose an option (1-3): "))
    
    if choice == 1:
        basic_operations()
    elif choice == 2:
        advanced_operations()
    elif choice == 3:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
