# 1. Python List Transformation

# Task 1: given the list of grades:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse = True)
print(grades)

# Task 2: Calculate the average grade and display it
import statistics
print(statistics.mean(grades))

# Task 3: Replace any grade below 80 with the value Failed
grades[7:10] = ["Failed", "Failed", "Failed"]
print(grades)

# 2. Advanced List Methods and Identity Operators

# Task 1: Given the two lists:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
matches = (i for i in submitted if i in attended)
print(matches)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.
print(submitted == attended)

#Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.
attended.remove("Eve")
attended.remove("Frank")
print(attended) 

# 3. Advanced Slicing Techniques

# Task 1: Given the list of temperatures:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[7:14])

# Task 2: Extract all the temperatures above 100.
print(temperatures[24:])

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
reversed_temps = temperatures[::-1]
print(reversed_temps[5:10])

# 4. Deep Dive into Python Lists

# Task 1: Given the lists:
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
# for (a,b,c,) in zip(students, grades, activities):
    # print(a,b,c)
student = students.pop(2)
grade = grades.pop(2)
activity = activities.pop(2)
print(student, grade, activity)

# Task 2: For the remaining students, add students name in a new list named students_approved.
students_approved = ["John", "Doe", "Smith"]

# Task 3: Print the list students_approved
print(students_approved)
