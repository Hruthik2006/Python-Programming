# Problem Statement 
# Develop a program to sort the contents of a text file and write the sorted contents into a separate text file.


def sort_file_contents(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as file:
            lines file.readlines()
        
        stripped_lines = [line.strip() for line in lines]
        stripped_lines.sort()

        for line in stripped_lines:
            file.write(line + '\n')
            print(f"Sorted contents have been written to 'output_file_path}'.")
            
    except FileNotFoundError:
            print(f"The file '{input_file_path}' was not found.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

input_file_path = input("Enter the path to the input text file: ")

output_file_path = input("Enter the path to the output text file: ")

sort_file_contents (input_file_path, output_file_path)

