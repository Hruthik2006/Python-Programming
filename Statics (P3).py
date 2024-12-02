# Problem Statement
# Read N numbers from the console and create a list. 
# Develop a program to print mean, variance and standard deviation with suitable messages.

import math

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance (numbers, mean):
    return sum((x mean) ** 2 for x in numbers) / len (numbers)

def calculate_standard_deviation (variance):
    return math.sqrt(variance)

n = int(input("Enter the number of elements (N): "))
numbers = []
for i in range(n):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

mean = calculate_mean(numbers)
variance calculate_variance (numbers, mean)
std_deviation = calculate_standard_deviation(variance)

print(f"\nMean: {mean:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")

