# Problem Statement
# Develop a program to read the student details like Name, USN, and Marks in three subjects. 
# Display the student details, total marks and percentage with suitable messages.

def input_student_details():
  name = input("Enter student's name: ")
  usn = input("Enter student's USN: ")
  marks = []

  for i in range(1, 4):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
  return name, usn, marks

def calculate_results (marks):
  total_marks = sum(marks)
  percentage = (total_marks / 300) 100 
  return total_marks, percentage

def display_student_details (name, usn, total_marks, percentage):
  print("\n--- Student Details ---")
  print(f"Name: {name}")
  print(f"USN: {usn}")
  print(f"Total Marks: {total_marks}")
  print(f"Percentage: {percentage:.2f}%")

name, usn, marks = input_student_details()

total_marks, percentage calculate_results (marks)

display_student_details (name, usn, total_marks, percentage)
