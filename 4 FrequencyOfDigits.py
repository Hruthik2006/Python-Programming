# Problem Statement 
# Read a multi-digit number (as chars) from the console. 
# Develop a program to print the frequency of each digit with suitable message.

def calculate_digit_frequency (number):
    frequency = {}
    for digit in number:
    if digit.isdigit():
        frequency [digit] = frequency.get(digit, 0) + 1
    return frequency

def display_digit_frequency(frequency):
    print("\nFrequency of each digit:")
    for digit, count in sorted(frequency.items()):
        print(f"Digit (digit}: {count} time(s)")

number input("Enter a multi-digit number: ")

frequency = calculate_digit_frequency (number)

display_digit_frequency (frequency)

