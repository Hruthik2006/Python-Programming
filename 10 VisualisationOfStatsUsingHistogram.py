# Problem Statement 
# Develop a program to generate a NumPy array of random integers. 
# Perform basic array operations such as finding the mean, median, variance, and standard deviation.
# Visualize the array values using a histogram.

import numpy as np
import matplotlib.pyplot as plt

def generate_random_array(size, low, high):
    return np.random.randint(low, high, size)

def array_operations (arr):
    mean = np.mean(arr)
    median = np.median(arr)
    variance = np.var(arr)
    std_deviation = np.std(arr)
    return mean, median, variance, std_deviation

def visualize_array_histogram(arr):
    plt.figure(figsize=(10, 6))
    plt.hist(arr, bins=10, edgecolor='black', alpha=0.7)
    plt.title('Histogram of Array Values')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

size = int(input("Enter the size of the array: "))
low = int(input("Enter the lower bound of the random integers: "))
high =  int(input("Enter the upper bound of the random integers: "))

arr generate_random_array (size, low, high)
print("\n Random array of integers is: \n", arr)

mean, median, variance, std_deviation = array_operations(arr)

print(f"\nArray Operations Results:")
print(f"Mean: {mean}")
print(f"Median: (median)")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")

visualize_array_histogram(arr)

